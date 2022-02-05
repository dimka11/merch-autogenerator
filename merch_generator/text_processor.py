from transformers import pipeline
from colour import Color
from deep_translator import GoogleTranslator
from natasha import Segmenter, MorphVocab, NewsEmbedding, NewsMorphTagger, NewsSyntaxParser, NewsNERTagger, PER, \
    NamesExtractor, Doc


class TextProcessor:
    def __init__(self):
        """Text processing class, load models for classification and NER Init time is very long (about 1 min) and download 4GB data at first start"""
        self.text_string: str
        self.ner_dict = {}
        self.sentence_lemmat_dict = {}
        self.sentence_lemmat = []
        self.translated_text = ""
        # init and download models ~ few minutes, about 4 GB download data
        print("start loading models")
        self.classifier = pipeline("zero-shot-classification", model='MoritzLaurer/mDeBERTa-v3-base-mnli-xnli',
                                   tokenizer='MoritzLaurer/mDeBERTa-v3-base-mnli-xnli', framework="pt")
        print("cls loaded")
        self.ner = pipeline("ner", grouped_entities=True, model='xlm-roberta-large-finetuned-conll03-english',
                            tokenizer='xlm-roberta-large-finetuned-conll03-english', framework="pt")
        print("ner loaded")

    def start_processing(self, text_str: str):
        """start processing the text string"""
        self.ner_dict = {}
        self.text_string = text_str
        self.classify_topic()
        self.create_lemmatization_dict()
        self.brand_and_location()
        self.merch_type()
        self.lemmatization()
        self.colors()
        self.text_desc()
        self.extras()
        self.brand2()

        return True  # always return true, yet

    def get_text_features_dict(self) -> dict:
        """Return the dict of features extracted from text string"""
        return self.ner_dict

    def classify_topic(self):
        topic_cats = ["конференция", "спорт", "концерт", "фестиваль", "выставка", "работа", "политика"]
        classifier_result = self.classifier(self.text_string, topic_cats,
                                            multi_label=False)  # по идее можно в конец перенести и использовать с отдельными словами мб как-то на качество повлияет
        # classifier(self.text_string, topic_cats, multi_label=True) # Попробовать с несколькими темами
        if classifier_result["scores"][0] > 0.35:
            self.ner_dict["topic"] = classifier_result["labels"][0]
        else:
            self.ner_dict["topic"] = None

    def create_lemmatization_dict(self):
        segmenter = Segmenter()
        morph_vocab = MorphVocab()
        emb = NewsEmbedding()
        morph_tagger = NewsMorphTagger(emb)
        syntax_parser = NewsSyntaxParser(emb)
        ner_tagger = NewsNERTagger(emb)
        names_extractor = NamesExtractor(morph_vocab)

        def extract_lemma(self, sen, return_dict=False):
            doc = Doc(sen)
            doc.segment(segmenter)
            doc.tag_morph(morph_tagger)
            doc.parse_syntax(syntax_parser)
            doc.tag_ner(ner_tagger)
            for token in doc.tokens:
                token.lemmatize(morph_vocab)
            if return_dict == False:
                return [token.lemma for token in doc.tokens]
            else:
                return {token.text: token.lemma for token in doc.tokens}

        self.sentence_lemmat = extract_lemma(self,
                                             self.text_string)  # " ".join([word.title() for word in sentences_lemmat[0]])
        self.sentence_lemmat_dict = extract_lemma(self, self.text_string, return_dict=True)

    def brand_and_location(self):
        # [word.title() for word in sentences[0].split()] Подумать, нужно ли делать капитализацию
        ner_result = self.ner(self.text_string)
        location = []
        organization = ""
        for item in ner_result:
            if (item["entity_group"] == 'ORG') or (item["entity_group"] == 'PER') or (item["entity_group"] == 'MISC'):
                organization = organization + " " + item["word"]
            if (item["entity_group"] == 'LOC'):
                location.append(item["word"])

        self.ner_dict["organization"] = organization

        if len(location) > 0:
            topic_cats0 = ["city", "country"]
            for item in location:
                cls_r = self.classifier(item, topic_cats0, multi_label=False)
            if cls_r["scores"][0] > 0.3:
                self.ner_dict[cls_r["labels"][0]] = item

    def merch_type(self):
        # Merch type тут тупо используем словарь
        self.ner_dict["merch_type"] = []
        metch_type_set = {"футболка", "толстовка", "майка", "майк", "блокнот"}
        [self.ner_dict["merch_type"].append(word) for word in self.sentence_lemmat if word in metch_type_set]

    def lemmatization(self):
        pass

    # merch_type_list = self.ner_dict["merch_type"]
    # merch_type_list_2 = []
    # for item in merch_type_list:
    #   merch_type_list_2.append(sentence_lemmat_dict[item])
    # self.ner_dict["merch_type"] = merch_type_list_2
    # self.ner_dict["city"] = sentence_lemmat_dict[ner_dict["city"]]
    # self.ner_dict["country"] = sentence_lemmat_dict[ner_dict["country"]]

    def colors(self):
        self.translated_text = GoogleTranslator(source='auto', target='en').translate(" ".join(self.sentence_lemmat))

        def check_color(color):
            try:
                color = color.replace(" ", "")
                Color(color)
                return True
            except ValueError:
                return False

        colors = []
        for idx, item in enumerate([check_color(word) for word in self.translated_text.split()]):
            if item == True:
                colors.append(self.translated_text.split()[idx])
        self.ner_dict["colors"] = colors

    def text_desc(self):
        text_desc_list = []

        translated_back_colors = []
        for item in self.ner_dict.get("colors"):
            translated = GoogleTranslator(source='auto', target='ru').translate(item)
            translated_back_colors.append(translated)

        for word in self.text_string.split():
            if len(translated_back_colors) > 0:
                if self.sentence_lemmat_dict.get(word) in translated_back_colors:
                    continue
            if self.ner_dict.get("topic") == word:
                continue
            if self.ner_dict.get("organization") == word:
                continue
            if self.ner_dict.get("city") == word:
                continue
            if self.ner_dict.get("country") == word:
                continue
            if self.ner_dict.get("merch_type") is not None:
                if self.sentence_lemmat_dict.get(word) in self.ner_dict.get("merch_type"):
                    continue
            if self.ner_dict.get("extra") is not None:
                if self.sentence_lemmat_dict.get(word) in self.ner_dict.get("extra"):
                    continue
            else:
                text_desc_list.append(word)


        self.ner_dict["design_pattern"] = " ".join(text_desc_list)


    def extras(self):
        self.ner_dict["extra"] = []
        find_dict = {"слова", "для", "поиска"}
        [self.ner_dict["extra"].append(word) for word in self.sentence_lemmat if word in find_dict]
        self.ner_dict["source_text_lemmas"] = self.sentence_lemmat

    def brand2(self):
        # Еще один способ поиска бренда :( работает плохо
        if self.ner_dict["organization"] == None:
            topic_cats_brand = ["company", "organization", "event", "brand"]
            for word in sentences_lemmat:
                cls_r = self.classifier(word, topic_cats_brand, multi_label=True)
            if cls_r["scores"][0] > len(topic_cats_brand) * 0.75:
                self.ner_dict["org0"] = word

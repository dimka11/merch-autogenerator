from text_processing import TextProcessing

if __name__ == "__main__":
	sentence1 = "Зеленая футболка Скуратова для турнир по шахматам в России в Омске"
	sentence2 = "красная зеленая Тамтэк для ит-конференции в Казахстане"
	sentence3 = "Синяя Luxoft для концерта в Ноябрьске клуб точка"
	sentence4 = "инсталяция фиолетовая для Burning man мясная лавка на Чили в Владивостоке"
	sentence5 = "мерч для Яндекса желтый с надписью Австралия"
	sentence6 = "Синяя майка Пекарушка для концерта в Ноябрьске клуб Точка"
	sentences = [sentence1, sentence2, sentence3, sentence4, sentence5, sentence6]
	# TEST_SEN_IDX = 3

	text_processing = TextProcessing()

	for sen in sentences:
		text_processing_result = text_processing.start_processing(sen)
		if text_processing_result == True:
		    text_features = text_processing.get_text_features_dict()
		if text_features is not None:
		    print(sen,'\n' ,text_features)
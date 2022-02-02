import numpy as np
import cv2
from .text_processor import TextProcessor
from .image_processor import ImgProcessor

class MerchGenerator:
    def __init__(self,
                 text_processor: TextProcessor,  # class for getting main features of merch from input string
                 img_processor: ImgProcessor,  # class for merch photo generation
                 ):
        self.text_processor = text_processor
        self.img_processor = img_processor

    def generate(
            self,
            img_description: str,  # text description of the image to be generated
    ) ->dict:
        text_processing_result = self.text_processor.start_processing(img_description)
        print(text_processing_result)
        merch_features_dict = self.text_processor.get_text_features_dict()
        print(merch_features_dict)
        # if merch_features_dict is not None:
        #     self.img_processor.run(merch_features_dict)


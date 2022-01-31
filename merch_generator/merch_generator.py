import numpy as np
import cv2
from text_processing import TextProcessing


class MerchGenerator:
    def __init__(self,
        text_string
                 text_processor,
                 img_processor.
                 ):
        self.text_string = text_string
        self.text_processor = text_processor
        self.img_processor = img_processor

    def generate(
            self,
            img_description: str,  # text description of the image to be generated
    ):
        text_string = self.text_string
        text_processing = text_processor # text_processor init outside ?
        text_processing_result = text_processing.start_processing(text_string)
        if text_processing_result == True:
            text_features = text_processing.get_text_features_dict()
        if text_features is not None:
            pass

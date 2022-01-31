import numpy as np
import cv2


class MerchGenerator:
    def __init__(self,
                 request_parser,
                 img_processor):
        self.request_parser = request_parser
        self.img_processor = img_processor

    def generate(
            self,
            img_description: str,  # text description of the image to be generated
    ):
        pass

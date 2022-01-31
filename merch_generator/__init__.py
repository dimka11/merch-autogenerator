from .merch_generator import MerchGenerator
from .text_processor import TextProcessor
from .image_processor import ImgProcessor

generator = MerchGenerator(img_processor=ImgProcessor(),
                           text_processor=TextProcessor())

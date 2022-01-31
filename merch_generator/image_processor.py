import cv2
import numpy as np

IMG_SIZE = 1024

class ImgProcessor:
    def __init__(self):
        self.img_size = IMG_SIZE
        self.logo_max_size = IMG_SIZE // 4
        self.country_flag_max_size = IMG_SIZE // 8

    def download_image(self, search_request_str: str):
        return np.ones((IMG_SIZE, IMG_SIZE, 4), dtype=np.uint8) * 127 + np.random.randint(-100, 100)

    def set_main_colour(self, img: np.ndarray, colour: str):
        loaded_img = self.download_image("цвет " + colour)
        return cv2.resize(loaded_img, (self.img_size, self.img_size))

    def add_design_pattern(self, img: np.ndarray, desing_pattern_name: str):
        loaded_img = self.download_image("дизайн паттерн " + desing_pattern_name)
        return cv2.resize(loaded_img, (self.img_size, self.img_size))

    def add_logo(self, img: np.ndarray, logo_name: str):
        loaded_img = self.download_image("логотип " + logo_name + " png")
        return cv2.resize(loaded_img, (self.logo_max_size, self.logo_max_size))

    def add_flag(self, img: np.ndarray, logo_name: str):
        loaded_img = self.download_image("флаг " + logo_name + " png")
        return cv2.resize(loaded_img, (self.logo_max_size, self.logo_max_size))

    def generate_merch_image(self, merch_features_dict):
        image = np.ones((IMG_SIZE, IMG_SIZE, 4), dtype=np.uint8) * 255
        image = self.set_main_colour(image, merch_features_dict['colour'])
        image = self.add_design_pattern(image, merch_features_dict['design_pattern'])
        image = self.add_flag(image, merch_features_dict['flag'])
        image = self.add_logo(image, merch_features_dict['brend'])
        return image
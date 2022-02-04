import cv2
import numpy as np

from YandexImagesParser.ImageParser import YandexImage
import requests


IMG_SIZE = 1024


class ImgProcessor:
    def __init__(self):
        self.img_size = IMG_SIZE
        self.logo_max_size = IMG_SIZE // 4
        self.country_flag_max_size = IMG_SIZE // 8
        self.img_search_parser = YandexImage()

    def download_image(self,
                       search_request_str: str,
                       img_format: str = 'jpg'):

        print(f"search \"{search_request_str}\"")
        search_result = self.img_search_parser.search(search_request_str)
        img_data = requests.get(search_result[0].preview.url).content
        with open(f'downloads/{search_request_str}.{img_format}', 'wb') as handler:
            handler.write(img_data)
        return cv2.imread(f'downloads/{search_request_str}.{img_format}')

    def set_main_colour(self, img: np.ndarray, colour: str):
        loaded_img = self.download_image(f"монотонный {colour} фон")
        print(f"set main colour: loaded_img.shape {loaded_img.shape} ")
        colour = np.dstack((loaded_img, np.ones(loaded_img.shape[:2],
                                                dtype=np.uint8) * 255))
        print(f"set main colour: colour.shape {colour.shape} ")
        return cv2.resize(colour, (self.img_size, self.img_size))

    def add_design_pattern(self, img: np.ndarray, desing_pattern_name: str):
        loaded_img = self.download_image(f"{desing_pattern_name} дизайн шаблон")
        print(type(loaded_img))
        print('design_pattern.shape', loaded_img.shape)
        design_pattern = cv2.resize(loaded_img, (self.img_size, self.img_size))
        design_pattern_gray = cv2.cvtColor(design_pattern, cv2.COLOR_BGR2GRAY)
        # create image in (c, h, w) format
        design_pattern_gray = np.stack((design_pattern_gray, design_pattern_gray, 
                                       design_pattern_gray, 
                                       np.ones(design_pattern_gray.shape, 
                                               dtype=np.uint8) * 255))
        # transform image to (h, w, c) format
        design_pattern_gray = design_pattern_gray.transpose(1, 2, 0)
        result = cv2.addWeighted(img, 0.5, design_pattern_gray, 0.5, 0)
        
        return result

    def add_logo(self, img: np.ndarray, logo_name: str):
        img_with_logo = img.copy()
        logo_img = self.download_image(f"логотип {logo_name} png", 'png')
        
        h, w = logo_img.shape[:2]
        resize_koef = self.logo_max_size / max(logo_img.shape)
        h, w = int(h * resize_koef), int(w * resize_koef)
        logo_resized = cv2.resize(logo_img, (w, h), cv2.INTER_LINEAR)
        logo_resized = np.dstack((logo_resized, np.ones(logo_resized.shape[:2],
                                                        dtype=np.uint8) * 255))

        CENTER_X, CENTER_Y = img.shape[:2]
        CENTER_X, CENTER_Y = CENTER_X // 2, CENTER_Y // 2
        h, w = logo_resized.shape[:2]
        x = CENTER_X - w // 2
        y = CENTER_Y - h // 2
        img_with_logo[y:y+h, x:x+w] = logo_resized
        
        return img_with_logo

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

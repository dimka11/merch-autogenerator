import cv2
import numpy as np

from merch_generator.image_processor import ImgProcessor

im_proc = ImgProcessor()

image = np.ones((1024, 1024, 4), dtype=np.uint8) * 255
image = im_proc.set_main_colour(image, "красный")
image = im_proc.add_design_pattern(image, "октябрьская революция")
image = im_proc.add_logo(image, "adidas")
cv2.imwrite('results/output.png', image)

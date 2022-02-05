import numpy as np
import cv2

from merch_generator import ImgProcessor

im_proc = ImgProcessor()


img = im_proc.generate_merch_image({
    'colour': "фиолетовая",
    'design_pattern': "для CompTech в Новосибирске",
    'brend': "puma",
})

cv2.imwrite("results/comptech_nsk_test_result.png", img)

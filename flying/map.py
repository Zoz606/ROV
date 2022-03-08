import cv2 as cv
import numpy as np
from findTheContour import *
from ColourDetector import *


class mapping:
    def __init__(self, img):
        self.img = img

    def map(self):
        # Create a white image
        zero = np.zeros([720, 1080, 1], np.uint8)
        zero.fill(255)

        return zero

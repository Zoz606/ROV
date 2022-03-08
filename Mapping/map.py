import cv2 as cv
import numpy as np
from ColourDetector import *


class mapping:
    def __init__(self, img):
        self.img = img

    def map(self):
        # Create a white image
        zero = np.zeros([720, 1080, 1], np.uint8)
        zero.fill(255)
        return zero

    def thresh(self):
        self.img = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        _, thresholdImg = cv.threshold(
            self.img, 127, 255, cv.THRESH_BINARY)
        return thresholdImg

    # def captureImg(self):

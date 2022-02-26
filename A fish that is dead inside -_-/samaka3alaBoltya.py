import cv2 as cv
import numpy as np
from ColourDetector import *


class samaka3laBoltya:
    def __init__(self, img):
        self.img = img

    def whiteEdgeCoordinates(self):
        lowerWhite, upperWhite = np.array([0, 0, 0]), np.array([0, 0, 255])
        whiteDetection = DetectColour(self.img, lowerWhite, upperWhite, 800)
        contour = whiteDetection.getcontours(self.img)

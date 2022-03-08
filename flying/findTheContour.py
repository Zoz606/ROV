from ColourDetector import *
import cv2 as cv
import numpy as np
from rangeOfColors import *

# color detection
def findTheContour(img, low, high):
    Colourdetection = DetectColour(img, low, high, 800)
    contours = Colourdetection.getcontours(img)
    if len(contours) > 0:
        return True
    else:
        return False

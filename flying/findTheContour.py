from ColourDetector import *
import cv2 as cv
import numpy as np

# Range of colors in hsv
lowerBlue, upperBlue = np.array([100, 150, 0]), np.array([140, 255, 255])
lowerRed, upperRed = np.array([159, 50, 70]), np.array([180, 255, 255])
lowerBlack, upperBlack = np.array([0, 0, 0]), np.array([180, 255, 30])


# color detection
def findTheContour(img, low, high):
    Colourdetection = DetectColour(img, low, high, 1000)
    contours = Colourdetection.getcontours(img)
    if len(contours) > 0:
        return True
    else:
        return False

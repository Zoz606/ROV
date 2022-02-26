import ColourDetector as cd
import cv2 as cv
import numpy as np

# Range of color red HSV
lowerRed, upperRed = np.array([159, 50, 70]), np.array([180, 255, 255])
# red Color detection


def findTheContour(img):
    Colourdetectio = cd.DetectColour(img, lowerRed, upperRed, 1000)
    contours = Colourdetectio.getcontours(img)
    if len(contours) > 0:
        return True
    else:
        return False

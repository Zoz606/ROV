import cv2 as cv
import numpy as np


def shapeDetection(img):
    # gaussian blur
    imgBlur = cv.GaussianBlur(img, (3, 3), 0)

    # Canny Edge Detection
    edges = cv.Canny(imgBlur, 200, 900)

    # drow a line to calculate the length
    edges = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)

    return edges

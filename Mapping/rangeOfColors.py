import cv2 as cv
import numpy as np

# Range of colors in hsv
lowerBlue, upperBlue = np.array([100, 0, 0]), np.array([140, 255, 255])
lowerRed, upperRed = np.array([170, 0, 0]), np.array([255, 255, 255])
lowerBlack, upperBlack = np.array([0, 0, 0]), np.array([180, 255, 30])
lowerBrown, upperBrown = np.array([10, 0, 0]), np.array([20, 255, 255])
lowerPink, upperPink = np.array([125, 0, 0]), np.array([158, 255, 255])

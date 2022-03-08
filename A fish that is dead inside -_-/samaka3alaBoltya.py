import cv2 as cv
import numpy as np
from ColourDetector import *


class samaka3laBoltya:
    def __init__(self, img):
        self.img = img

    def whiteEdgeCoordinates(self):
        lowerWhite, upperWhite = np.array([0, 0, 255]), np.array([359, 0, 255])
        whiteDetection = DetectColour(self.img, lowerWhite, upperWhite, 800)
        contour = whiteDetection.getcontours(self.img)

        for cnt in contour:
            approx = cv.approxPolyDP(
                cnt, 0.009 * cv.arcLength(cnt, True), True)
            # draws boundary of contours.
            cv.drawContours(self.img, [approx], 0, (0, 0, 255), 5)

            # Used to flatted the array containing
            # the co-ordinates of the vertices.
            boundriesOfTheContour = approx.ravel()
            counter = 0

            for j in boundriesOfTheContour:
                if counter % 2 == 0:
                    x = boundriesOfTheContour[counter]
                    y = boundriesOfTheContour[counter + 1]

                    # text on remaining co-ordinates.
                    cv.putText(self.img, f'({x}, {y})', (x, y),
                               cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))
                counter += 1

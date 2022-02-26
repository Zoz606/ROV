import cv2 as cv
import numpy as np
from edgesOfTheFish import *


cap = cv.VideoCapture(1)


while True:
    _, frame = cap.read()

    template = cv.imread('fish.jpg', 0)
    template = cv.resize(template, (900, 400))
    templateEdges = shapeDetection(template)

    cv.imshow('img', template)
    cv.imshow('LIVE', frame)
    cv.imshow('edge', templateEdges)

    if cv.waitKey(1) == 27:
        break

cap.release()
cv.destroyAllWindows()

'''
        res = cv.matchTemplate(gray, template, cv.TM_SQDIFF)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        top_left = min_loc
        bottom_right = (top_left[0] + 900, top_left[1] + 400)

        cv.rectangle(frame, top_left, bottom_right, 255, 1)
'''

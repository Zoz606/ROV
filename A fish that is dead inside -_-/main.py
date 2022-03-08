import cv2 as cv
import numpy as np
from edgesOfTheFish import *
from samaka3alaBoltya import samaka3laBoltya


cap = cv.VideoCapture(1)


while True:
    _, frame = cap.read()

    template = cv.imread('fish.jpg', 0)
    template = cv.resize(template, (900, 400))
    templateEdges = shapeDetection(template)

    samaka = samaka3laBoltya(templateEdges)
    samaka.whiteEdgeCoordinates()

    cv.imshow('img', template)
    cv.imshow('LIVE', frame)
    cv.imshow('edge', templateEdges)

    if cv.waitKey(1) == 27:
        break

cap.release()
cv.destroyAllWindows()

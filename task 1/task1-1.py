import cv2 as cv
import numpy as np
from ColourDetector import *

# range of the color brown
lowBrown, highBrown = np.array([10, 0, 0]), np.array([20, 255, 255])

# capture the video
cap = cv.VideoCapture(0)
#frame = cv.imread('1.png')


while True:
    _, frame = cap.read()

    # detection of the brown color and draw the contour around it
    colorDetection = DetectColour(frame, lowBrown, highBrown, 800)
    contours = colorDetection.getcontours(frame)
    frame = cv.drawContours(frame, contours, 1, (255, 0, 0), 1)

    for contour in contours:
        # initializ the shape name and approximate the contour
        perimeter = cv.arcLength(contour, True)
        approximate = cv.approxPolyDP(contour, 0.01 * perimeter, True)

        # finding center point of shape
        M = cv.moments(contour)
        if M['m00'] != 0.0:
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])

        cv.putText(frame, 'Damaged part', (x, y),
                   cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1)

    cv.imshow('LIVE', frame)
    if cv.waitKey(1) == 27:
        break

cap.release()
cv.destroyAllWindows()

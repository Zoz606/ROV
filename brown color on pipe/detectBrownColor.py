import cv2 as cv
import numpy as np
from ColourDetector import *


def detectBrownColor():
    # capture the video
    # cap = cv.VideoCapture('rtsp://admin:adminrov1234@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0') #ROV cam
    # cap = cv.VideoCapture(3)  # Mobile cam
    cap = cv.VideoCapture(1)  # Labtop cam

    #frame = cv.imread('1.png')

    while True:
        _, frame = cap.read()

        # detection of the brown color and draw the contour around it
        colorDetection = DetectColour(frame, lowerBrown, upperBrown, 800)
        contours = colorDetection.getcontours(frame)
        frame = cv.drawContours(frame, contours, 1, (255, 0, 0), 1)

        for contour in contours:

            # finding center point of shape
            M = cv.moments(contour)
            if M['m00'] != 0.0:
                x = int(M['m10']/M['m00'])
                y = int(M['m01']/M['m00'])

            cv.putText(frame, 'Damaged part', (x+50, y+50),
                       cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1)

        cv.imshow('LIVE', frame)
        if cv.waitKey(1) == 27:
            break

    cap.release()
    cv.destroyAllWindows()


detectBrownColor()

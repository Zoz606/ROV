import cv2 as cv
from ColourDetector import *


def detectOrangeColor():
    # capture the video
    # cap = cv.VideoCapture('rtsp://admin:adminrov1234@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0') #ROV cam
    # cap = cv.VideoCapture(3)  # Mobile cam
    cap = cv.VideoCapture(1)  # Labtop cam
    #frame = cv.imread('1.png')

    while True:
        _, frame = cap.read()

        # detection of the brown color and draw the contour around it
        colorDetection = DetectColour(frame, lowerOrange, upperOrange, 800)
        contours = colorDetection.getcontours(frame)
        frame = cv.drawContours(frame, contours, 0, (255, 0, 0), 1)

        cv.imshow('LIVE', frame)

        if cv.waitKey(1) == 27:
            break

    cap.release()
    cv.destroyAllWindows()


detectOrangeColor()

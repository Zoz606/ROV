import cv2 as cv
from ColourDetector import *
from saveImg import *


startPoint = False
endPoint = False

# Operation:
# click on the up left of the contour then on the bottm right, it draws a rectangle between the two points,
# then on the third click it show the image inside the rectangle and save it


def clickEvent(event, x, y, flags, params):
    global line, startPoint, endPoint, screenshot
    # get mouse click
    if event == cv.EVENT_LBUTTONDOWN:
        if startPoint == True and endPoint == True:
            startPoint = False
            endPoint = False
            #line = (0, 0, 0, 0)
        elif startPoint == False:
            line = (x, y, 0, 0)
            startPoint = True
        elif endPoint == False:
            line = (line[0], line[1], x, y)
            endPoint = True
        screenshot = frame[line[1]: line[3], line[0]: line[2]]
        if startPoint == False and endPoint == False:
            cv.imshow('screenshot', screenshot)
            saveImage(screenshot)


# cap = cv.VideoCapture('rtsp://admin:adminrov1234@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0')  # ROV cam
cap = cv.VideoCapture(1)  # Labtop cam
# cap = cv.VideoCapture(0)  # Mobile cam

stitchCounter = 1

while True:
    # if stitchCounter < 8:
    _, frame = cap.read()
    frame = cv.resize(frame, (1000, 700))

    cv.namedWindow('LIVE')
    cv.setMouseCallback('LIVE', clickEvent)

    if startPoint == True and endPoint == True:
        cv.rectangle(frame, (line[0], line[1]),
                     (line[2], line[3]), (255, 0, 0), 1)

    cv.imshow('LIVE', frame)
    stitchCounter += 1

    # elif stitchCounter == 8:

    if cv.waitKey(1) == 27:
        break
cap.release()
cv.destroyAllWindows()

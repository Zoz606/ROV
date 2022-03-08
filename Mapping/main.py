import cv2 as cv
from ColourDetector import *
from saveImg import *


startPoint = False
endPoint = False


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


# cap = cv.VideoCapture('rtsp://admin:adminrov1234@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0') #ROV cam
cap = cv.VideoCapture(1)  # Labtop cam
# cap = cv.VideoCapture(0)  # Mobile cam

while True:
    _, frame = cap.read()
    cv.namedWindow('LIVE')
    cv.setMouseCallback('LIVE', clickEvent)

    if startPoint == True and endPoint == True:
        cv.rectangle(frame, (line[0], line[1]),
                     (line[2], line[3]), (255, 0, 0), 2)
    cv.imshow('LIVE', frame)

    if cv.waitKey(1) == 27:
        break
cap.release()
cv.destroyAllWindows()

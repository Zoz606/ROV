import cv2 as cv
from findTheContour import *

#cap = cv.VideoCapture('rtsp://admin:adminrov1234@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0')
cap = cv.VideoCapture(0)
counter = 0


while True:
    _, frame = cap.read()

    # detect the region of intrest
    x = frame.shape[0]
    y = frame.shape[1]
    leftRegion = frame[:x, :200]
    topRegion = frame[:100, 200: y - 200]
    rightRegion = frame[:x, y - 200: y]
    botRegion = frame[x - 100: x, 200: y - 200]

    # color detection
    leftContour = findTheContour(leftRegion)
    topContour = findTheContour(topRegion)
    rightContour = findTheContour(rightRegion)
    botContour = findTheContour(botRegion)

    # put text
    cv.putText(leftRegion, f"ContaingRed:{leftContour}",
               (20, 80), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

    cv.putText(topRegion, f"ContaingRed:{topContour}",
               (20, 80), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

    cv.putText(rightRegion, f"ContaingRed:{rightContour}",
               (20, 80), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

    cv.putText(botRegion, f"ContaingRed:{botContour}",
               (20, 80), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

    # print(leftContour)
    # print(topContour)
    # print(rightContour)
    # print(botContour)

    # initializing the movment by moving forward from the top left side
    if topContour and botContour and counter == 0:
        cv.putText(frame, "continue moving forward", (10, 20),
                   cv.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 1)

    # moving right when detecting the 1rd courner
    if rightContour and botContour:
        cv.putText(frame, "Go right", (10, 20),
                   cv.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 1)

    # Continue moving right till the ROV reaches the 2nd corner
    if leftContour and rightContour:
        cv.putText(frame, "Continue moveing to right", (10, 20),
                   cv.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 1)

    # going down when detecting the 2nd courner
    if leftContour and botContour:
        cv.putText(frame, "Go backward", (10, 20),
                   cv.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 1)
        counter += 1

    # continue moving left on the second vertical line
    if topContour and botContour and counter > 0:
        cv.putText(frame, "Continue moving Backward", (10, 20),
                   cv.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 1)

        counter = 0

    # start to move right when detecting the 4rth corner
    if topContour and rightContour:
        cv.putText(frame, "Go right", (10, 20),
                   cv.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 1)

    # start to move left when detecting the second corner
    if topContour and leftContour:
        cv.putText(frame, "Go forward", (10, 20),
                   cv.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 1)

    cv.imshow('video', frame)
    cv.imshow('top', topRegion)
    cv.imshow('bot', botRegion)
    cv.imshow('right', rightRegion)
    cv.imshow('left', leftRegion)

    if cv.waitKey(1) == 27:
        break
cap.release()
cv.destroyAllWindows()

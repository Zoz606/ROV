import cv2 as cv
from findTheContour import *

# cap = cv.VideoCapture('rtsp://admin:adminrov1234@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0') #ROV cam
cap = cv.VideoCapture(1)  # Labtop cam
# cap = cv.VideoCapture(0) #Mobile cam

while True:
    _, frame = cap.read()
    frame = cv.resize(frame, (900, 700))

    # detect the region of intrest
    x = frame.shape[0]
    y = frame.shape[1]
    leftRegion = frame[:x, :160]
    topRegion = frame[:100, 160: y - 160]
    rightRegion = frame[:x, y - 160: y]
    botRegion = frame[x - 100: x, 160: y - 160]

    # Blue detection in top and bottom regions
    topContourBlue = findTheContour(topRegion, lowerBlue, upperBlue)
    botContourBlue = findTheContour(botRegion, lowerBlue, upperBlue)

    cv.putText(topRegion, f"ContaingBlue:{topContourBlue}",
               (60, 20), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

    cv.putText(botRegion, f"ContaingBlue:{botContourBlue}",
               (60, 20), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

    # black detection in top and botom regions
    topContourBlack = findTheContour(topRegion, lowerBlack, upperBlack)
    botContourBlack = findTheContour(botRegion, lowerBlack, upperBlack)

    cv.putText(topRegion, f"ContaingBlack:{topContourBlack}",
               (60, 40), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

    cv.putText(botRegion, f"ContaingBlack:{botContourBlack}",
               (60, 40), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

    # Red detection in right and left regions
    rightContourRed = findTheContour(rightRegion, lowerRed, upperRed)
    leftContourRed = findTheContour(leftRegion, lowerRed, upperRed)

    cv.putText(leftRegion, f"ContaingRed:{leftContourRed}",
               (5, 220), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

    cv.putText(rightRegion, f"ContaingRed:{rightContourRed}",
               (5, 220), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

    # if You detect the red line on the right move a little to the left
    if rightContourRed and not leftContourRed:
        cv.putText(frame, 'Move a little to the left', (400, 100),
                   cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)

    # if You detect the red line on the left move a little to the right
    if leftContourRed and not rightContourRed:
        cv.putText(frame, 'Move a little to the right', (5, 100),
                   cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)

    # if You detect both the red line on the right and the left get closer o the ground
    if leftContourRed and rightContourRed:
        cv.putText(frame, 'Get a little closer', (240, 200),
                   cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)

    # start moving forward when detecting the black Vertical line in the start
    if not leftContourRed and not rightContourRed:
        if topContourBlack and topContourBlue:
            cv.putText(frame, 'Go forward', (250, 350),
                       cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)

        # Stop the movement when detecting the black Vertical line in the End
        if botContourBlack and botContourBlue:
            cv.putText(frame, 'STOP!!', (270, 100),
                       cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)

        # Continue moving forward till you end the blue lines
        if topContourBlue and botContourBlue:
            cv.putText(frame, 'Continue moving forward', (200, 200),
                       cv.FONT_HERSHEY_COMPLEX, 0.5, (89, 257, 187), 1)

    cv.imshow('LIVE', frame)
    cv.imshow('top', topRegion)
    cv.imshow('bot', botRegion)
    cv.imshow('right', rightRegion)
    cv.imshow('left', leftRegion)

    if cv.waitKey(1) == 27:
        break

cap.release()
cv.destroyAllWindows()

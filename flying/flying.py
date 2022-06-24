import cv2 as cv
from findTheContour import *
from Motion import *


def flying():
    # cap = cv.VideoCapture('rtsp://admin:adminrov1234@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0') #ROV cam
    cap = cv.VideoCapture(0)  # Mobile cam
    # cap = cv.VideoCapture(1)  # Labtop cam

    while True:
        _, frame = cap.read()
        frame = cv.resize(frame, (950, 700))

        # detect the region of intrest
        h = frame.shape[0]
        w = frame.shape[1]
        leftRegion = frame[:h, :160]
        topRegion = frame[:100, 160: w - 160]
        rightRegion = frame[:h, w - 160: w]
        botRegion = frame[h - 100: h, 160: w - 160]
        midRegion = frame[100: h - 100, 160: w - 160]
        leftHalfRegion = frame[:h, :int(w/2)]
        rightHalfRegion = frame[:h, int(w/2): w]

        ############################################################## COLORS ##################################################
        # Blue detection in top and bottom regions
        topContourBlue = findTheContour(topRegion, lowerBlue, upperBlue)
        botContourBlue = findTheContour(botRegion, lowerBlue, upperBlue)
        rightContourBlue = findTheContour(
            rightHalfRegion, lowerBlue, upperBlue)
        leftContourBlue = findTheContour(leftHalfRegion, lowerBlue, upperBlue)

        # black detection in top and botom regions
        ContourBlack = findTheContour(midRegion, lowerBlack, upperBlack)

        # Red detection in rightHalfRegion and leftHalfRegion regions
        rightContourRed = findTheContour(rightRegion, lowerRed, upperRed)
        leftContourRed = findTheContour(leftRegion, lowerRed, upperRed)

        ########################################################## GUI 3ala 2ad 7aloo keda ###################################
        cv.putText(topRegion, f"Blue:{topContourBlue}",
                   (60, 20), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

        cv.putText(botRegion, f"Blue:{botContourBlue}",
                   (60, 20), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

        cv.putText(leftHalfRegion, f"Blue:{leftContourBlue}",
                   (120, 220), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

        cv.putText(rightHalfRegion, f"Blue:{rightContourBlue}",
                   (100, 220), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

        cv.putText(midRegion, f"Black:{ContourBlack}",
                   (60, 40), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

        cv.putText(leftRegion, f"Red:{leftContourRed}",
                   (5, 220), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

        cv.putText(rightRegion, f"Red:{rightContourRed}",
                   (80, 220), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

        ############################################################# I LIKE TO MOVE IT MOVE IT #############################

        # Start movement
        if (ContourBlack) and (not (rightContourRed or leftContourRed)) and (rightContourBlue and leftContourBlue):
            cv.putText(frame, 'Start moving forward', (400, 300),
                       cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 200), 1)

        # Continue moving forward till you end the blue lines
        if (not ContourBlack) and (leftContourBlue and rightContourBlue) and (not (rightContourRed or leftContourRed)):
            cv.putText(frame, 'Go forward', (200, 200),
                       cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 187), 1)

        if (not ContourBlack) and ((leftContourBlue and not rightContourBlue) or (rightContourBlue and not leftContourBlue) or (rightContourRed or leftContourRed)):
            cv.putText(frame, 'Stop the movement and start from the beginning', (100, 200),
                       cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 187), 1)

        # Stop the movement when detecting the black Vertical line in the End
        if (ContourBlack and botContourBlue):
            cv.putText(frame, 'STOP!!', (270, 100),
                       cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)
            leftContourBlue = False
            rightContourBlue = False

        cv.imshow('LIVE', frame)
        #cv.imshow('top', topRegion)
        #cv.imshow('bot', botRegion)
        #cv.imshow('rightHalfRegion', rightRegion)
        #cv.imshow('leftHalfRegion', leftRegion)
        #cv.imshow('mid', midRegion)
        #cv.imshow('leftHalfRegion', leftHalfRegion)
        #cv.imshow('rightHalfRegion', rightHalfRegion)

        if cv.waitKey(1) == 27:
            break

    cap.release()
    cv.destroyAllWindows()


flying()

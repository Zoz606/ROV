import cv2 as cv

#cap = cv.VideoCapture(1)
cap = cv.VideoCapture(
    'rtsp://admin:adminrov1234@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0')  # ROV cam

while True:
    _, frame = cap.read()
    frame = cv.flip(frame, 0)
    #frame = cv.flip(frame, 1)

    cv.imshow('frame', frame)
    if cv.waitKey(1) == 27:
        break

cap.release()
cv.destroyAllWindows()

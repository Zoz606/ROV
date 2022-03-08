import math
import cv2
cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 1080)
startPoint = False
endPoint = False


def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1-x2, 2)+math.pow(y1-y2, 2))


def on_mouse(event, x, y, flags, params):
    global line, startPoint, endPoint
    # get mouse click
    if event == cv2.EVENT_LBUTTONDOWN:
        if startPoint == True and endPoint == True:
            startPoint = False
            endPoint = False
            line = (0, 0, 0, 0)
        if startPoint == False:
            line = (x, y, 0, 0)
            startPoint = True
        elif endPoint == False:
            line = (line[0], line[1], x, y)
            endPoint = True


calibration = False
ratio = 0.0
while True:
    ret, img = cap.read()
    cv2.namedWindow('frame')
    cv2.setMouseCallback('frame', on_mouse)
    if startPoint == True and endPoint == True:
        if not(calibration):
            cv2.line(img, (line[0], line[1]),
                     (line[2], line[3]), (255, 0, 255), 2)
            ratio = distance(line[0], line[1], line[2], line[3])/20
            calibration = True
        else:
            cv2.line(img, (line[0], line[1]),
                     (line[2], line[3]), (255, 0, 255), 2)
        cv2.putText(img, f"The distance is{(1/ratio)*distance(line[0],line[1],line[2],line[3])}cm", (
            50, 80), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
    cv2.imshow('frame', img)
    key = cv2.waitKey(1)
    if key == 27:
        break

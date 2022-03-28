import cv2 as cv
from djitellopy import tello
import cvzone

cap = cv.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

classNames = []
classFile = 'coco.names'

with open(classFile, 'rt') as f:
    classNames = f.read().split('\n')
 
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weghtsPath = 'frozen_inference_graph.pb'

net = cv.dnn_DetectionModel(weghtsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)



#print(classNames)

while True:
    ret, frame = cap.read()

    cv.imshow('LIVE', frame)

    if cv.waitKey(1) == 27:
        break

cap.release()
cv.destroyAllWindows()

'''
cap = cv.VideoCapture(1)


while True:
    _, frame = cap.read()

    template = cv.imread('fish.jpg', 0)
    template = cv.resize(template, (900, 400))
    templateEdges = shapeDetection(template)

    samaka = samaka3laBoltya(templateEdges)
    samaka.whiteEdgeCoordinates()

    cv.imshow('img', template)
    cv.imshow('LIVE', frame)
    cv.imshow('edge', templateEdges)

    if cv.waitKey(1) == 27:
        break

cap.release()
cv.destroyAllWindows()
'''

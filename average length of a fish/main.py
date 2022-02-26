import cv2 as cv
import numpy as np

import math
import matplotlib.pyplot as plt


def distanceCalculate(p0, p1):  # p1 and p2 in format (x1,y1) and (x2,y2) tuples
    dis = math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
    return dis


def click_event(event, x, y, flags, params):
    point = []
    # checking for left mouse clicks
    if event == cv.EVENT_LBUTTONDOWN:
        point.append(x)
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)

        # displaying the coordinates
        # on the image window
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(edges, str(x) + ',' + str(y),
                   (x, y), font, 1, (255, 0, 0), 2)
        cv.imshow('Canny Edge Detection', edges)
        return point


# read the original image
originalImg = cv.imread('fish.jpg')
resizedOriginalImg = cv.resize(originalImg, (900, 400))

# gaussian blur
imgBlur = cv.GaussianBlur(resizedOriginalImg, (3, 3), 0)

# Combined X and Y Sobel Edge Detection
sobelxy = cv.Sobel(imgBlur, cv.CV_64F, 1, 1, 5)

# Canny Edge Detection
edges = cv.Canny(imgBlur, 200, 900)

# drow a line to calculate the length
edges = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)


# Show resultes
cv.imshow('originalImg', resizedOriginalImg)
cv.imshow('Canny Edge Detection', edges)
cv.setMouseCallback('Canny Edge Detection', click_event)

# while True:
#p0 = []
#p1 = [2]
#p0.append(cv.setMouseCallback('Canny Edge Detection', click_event))
#p1.append(cv.setMouseCallback('Canny Edge Detection', click_event))
# print(p0)
#distance = distanceCalculate(p0, p1)
#print(f'distance = {distance}')
#cv.imshow('Sobel X Y using Sobel() function', sobelxy)
#cv.imshow('gaussian', imgBlur)


cv.waitKey()
cv.destroyAllWindows()

'''def drawLine(edges, event, x, y, flags):
    global p0, p1

    if event == cv.EVENT_LBUTTONDOWN:
        p0 = x, y
        p1 = x, y

    elif event == cv.EVENT_MOUSEMOVE and flags == 1:
        p1 = x, y

    elif event == cv.EVENT_LBUTTONUP:
        p1 = x, y

    cv.line(edges, p0, p1, (0, 0, 255), 2)

    cv.imshow('Canny Edge Detection', edges)
'''

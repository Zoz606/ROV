import cv2 as cv
import numpy as np


counter = 1


def resizeImg(img):
    resizedImg = cv.resize(img, (150, 180))
    return resizedImg


def saveImg(screenshot):
    global counter
    # Save the screenshot before edit
    cv.imwrite(f'{counter}.jpg', screenshot)

    # Resize every screenshot to make it posible to attach them together
    img = cv.imread(f'{counter}.jpg')
    resizedImg = resizeImg(img)

    # Save the screenshot after editting
    cv.imwrite(f'{counter}.jpg', resizedImg)
    # Show every screenshot
    cv.imshow(f'{counter}', resizedImg)

    counter += 1

    if counter > 8:
        evenList = []
        oddList = []
        for evenCounter in range(2, 9, 2):
            evenList.append(cv.imread(f'{evenCounter}.jpg'))
        evenList.reverse()

        for oddCounter in range(1, 8, 2):
            oddList.append(cv.imread(f'{oddCounter}.jpg'))
        oddList.reverse()

        horizontalEvenImg = cv.vconcat(evenList)
        horizontalOddImg = cv.vconcat(oddList)
        totalMap = cv.hconcat([horizontalEvenImg, horizontalOddImg])
        #cv.imshow('even', horizontalEvenImg)
        #cv.imshow('odd', horizontalOddImg)
        cv.imshow('MAP', totalMap)
        cv.imwrite('Map.jpg', totalMap)

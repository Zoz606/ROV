import cv2 as cv
import numpy as np


counter = 1


def resizeImg(img):
    resizedImg = cv.resize(img, (200, 300))
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

    if counter == 8:
        evenList = []
        oddList = []
        for evenCounter in range(2, 8, 2):
            evenList.append(f'{evenCounter}.jpg')

        for oddCounter in range(1, 7, 2):
            oddList.append(f'{oddCounter}.jpg')
            
        for i in range(0, 4):
            horizontalEvenImg = np.concatenate((evenList[i], evenList[i + 1]))

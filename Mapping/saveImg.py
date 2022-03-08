import cv2 as cv

counter = 1


def saveImage(screenshot):
    global counter
    cv.imwrite(f'screenshot number {counter}.png', screenshot)
    counter = counter + 1

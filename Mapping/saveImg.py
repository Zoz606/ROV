import cv2 as cv


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

    counter = counter + 1


'''   if counter % 2 == 0:
        cv.hconcat()
'''

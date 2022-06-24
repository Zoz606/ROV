import cv2 as cv



counter = 1


class saveResizeMapping():
    def __init__(self, screenshot):
        self.screenshot = screenshot

    # resize every image to make it possible to attach them together
    def resizeImg(self, img):
        resizedImg = cv.resize(img, (150, 180))
        return resizedImg

    #
    def saveImg(self):
        global counter
        # Save the screenshot before edit
        cv.imwrite(f'{counter}.jpg', self.screenshot)

        # Resize every screenshot to make it posible to attach them together
        img = cv.imread(f'{counter}.jpg')
        resizedImg = self.resizeImg(img)

        # Save the screenshot after editting
        cv.imwrite(f'{counter}.jpg', resizedImg)
        # Show every screenshot
        cv.imshow(f'{counter}', resizedImg)

        counter += 1

        # Drawing the map
        if counter > 8:
            evenList = []
            oddList = []
            # Make a list of the left squares (the even pics)
            for evenCounter in range(2, 9, 2):
                evenList.append(cv.imread(f'{evenCounter}.jpg'))
            evenList.reverse()

            # Make a list of the right squares (the odd pics)
            for oddCounter in range(1, 8, 2):
                oddList.append(cv.imread(f'{oddCounter}.jpg'))
            oddList.reverse()

            # attach even pics together and the odd pics together
            horizontalEvenImg = cv.vconcat(evenList)
            horizontalOddImg = cv.vconcat(oddList)

            # The whole GOD DAMMN map
            totalMap = cv.hconcat([horizontalEvenImg, horizontalOddImg])
            #cv.imshow('even', horizontalEvenImg)
            #cv.imshow('odd', horizontalOddImg)

            # show and save the map
            cv.imshow('MAP', totalMap)
            cv.imwrite('Map.jpg', totalMap)

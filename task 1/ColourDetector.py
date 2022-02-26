import cv2
import numpy as np


class DetectColour:
    def __init__(self, img, colourlow, colourhigh, tolerance):
        self.img = img  # Passing the image to class after read it in main
        # take the lowe of the color and save it
        self.lower_colour = np.array(colourlow)
        # take the higher of the color and save it
        self.upper_colour = np.array(colourhigh)
        # tolerance to adjust the area of the contours we need to get
        self.tolerance = tolerance

    def getcontours(self, img1):
        # read the image as hsv
        self.hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
        # get the mask of the color
        self.mask = cv2.inRange(self.hsv, self.lower_colour, self.upper_colour)
        # get the gradient of the mask and the image by all ones so we remove any parts black and remains the white
        gradient = cv2.morphologyEx(
            self.mask, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))
        # now we get the contours for any parts white
        contours, _ = cv2.findContours(
            gradient, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        newcontourslist = []  # list to contains what we will use from those contours
        for i in range(len(contours)):
            # here we loop in contours and find there area if its larger than the tolerance will save them in new list
            if cv2.contourArea(contours[i]) > self.tolerance:
                # append what we need in new list
                newcontourslist.append(contours[i])
        contours = newcontourslist  # passing the list to contours
        return contours  # return the contours to athoer function

    def show(self, video, cap):
        if video == True:
            # will capture the cam video if we not passing an path or link for DVR
            cap = cap
            while cap.isOpened():  # chck if the cam is opened
                ret, im = cap.read()  # get every frame in image
                # draw the contours from above function to on the video by passing every frame to it
                cv2.drawContours(im, self.getcontours(
                    im), -1, (100, 255, 60), 3)
                return im
        else:
            # print(self._getcontours())
            cv2.drawContours(self.img, self.getcontours(
                self.img), -1, (255, 0, 0), 2)
            return self.img

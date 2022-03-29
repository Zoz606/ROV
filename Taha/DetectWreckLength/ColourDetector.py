import cv2
import numpy as np
class DetectColour:
    def __init__(self,img,colourlow,colourhigh,tolerance):
        self.img=img  ##Passing the image to class after read it in main
        self.lower_colour = np.array(colourlow) #take the lowe of the color and save it
        self.upper_colour = np.array(colourhigh) #take the higher of the color and save it
        self.tolerance=tolerance #tolerance to adjust the area of the contours we need to get
    def getcontours(self,img1):
        self.hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV) #read the image as hsv
        mask = cv2.inRange(self.hsv, self.lower_colour, self.upper_colour) #get the mask of the color
        gradient = cv2.morphologyEx(mask, cv2.MORPH_CLOSE,np.ones((3, 3), np.uint8))# get the gradient of the mask and the image by all ones so we remove any parts black and remains the white
        contours, hierarchy = cv2.findContours(gradient, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)##now we get the contours for any parts white
        newcontourslist=[] #list to contains what we will use from those contours
        for i in range(len(contours)):
            if cv2.contourArea(contours[i]) > self.tolerance:  ##here we loop in contours and find there area if its larger than the tolerance will save them in new list
                newcontourslist.append(contours[i]) ##append what we need in new list
        contours=newcontourslist ##passing the list to contours
        return contours ## return the contours to athoer function
    def show(self,video,path=0):
        if  video==True:
            cap=cv2.VideoCapture(path) ## will capture the cam video if we not passing an path or link for DVR
            while cap.isOpened(): ##chck if the cam is opened
                ret,im=cap.read() ##get every frame in image
                cv2.drawContours(im,self.getcontours(im),-1,(0,255,0),3) ##draw the contours from above function to on the video by passing every frame to it
                cv2.imshow("Video",im)##Showing the frame
                if cv2.waitKey(1)==ord('q'):
                    break ##wait to any key for close
        else:
            ##print(self._getcontours())
            cv2.drawContours(self.img,self.getcontours(self.img),-1,(255,0,0),2)
            cv2.imshow("Image",self.img)
            cv2.waitKey(0)

# lower_red = np.array([159,50,70]) ##the lower variable for the red
# upper_red = np.array([180,255,255])## the upper variable for the red
# img=cv2.imread("img_2.png") #takes an image or you can pass true to show to use video
# Colourdetectio=DetectColour(img,lower_red,upper_red,100) ##creat an object of the class
# Colourdetectio.show(False) #send to show false meaning we will used the img not video send true only meaing we will use the cam video send true ant the link or path for video or dvr to can use them









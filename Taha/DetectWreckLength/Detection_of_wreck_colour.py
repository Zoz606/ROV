#  Modules
import cv2
import math
from ColourDetector import DetectColour
import numpy as np 
#  Declearation 
lowerBlue, upperBlue = np.array([90, 50, 70]), np.array([128, 255, 255])
lowBrown, upperBrown = np.array([10, 0, 0]), np.array([20, 255, 255])
Distance_between_two_blue_line_in_cm=20
# Function to get the contour exists or not 
def get_the_coutours(img):
    Colourdetectio=DetectColour(img,lowerBlue,upperBlue,800) ##creat an object of the class)
    contours=Colourdetectio.getcontours(img)
    imgmask=np.ones([img.shape[0],img.shape[1],3],dtype=np.uint8)
    imgmask=cv2.drawContours(imgmask,contours,-1,(255,255,255),-1)
    if len(contours)>0:
        return True
    else:
        return False
#  Function to compute the distance between the two points in pixels 
def compute_distance(x1,y1,x2,y2):
    return math.sqrt(((x1-x2)**2)+((y1-y2)**2))
# start the camera take care to change it according to ur web cam 
cap=cv2.VideoCapture(1)
while True:
    ret,frame=cap.read()
    h,w,c=frame.shape
    w1=w//3
    w2=w*2//3
    img2=frame[:,w2:]
    img1=frame[:,:w1]
    # Print the state of every side of frame to check if there is blue 
    cv2.putText(frame,f"ContaingBlue:{get_the_coutours(img1)}",(w1-200,200),cv2.FONT_HERSHEY_PLAIN,0.8,(255,0,0),1)
    cv2.putText(frame,f"ContaingBlue:{get_the_coutours(img2)}",(w2,200),cv2.FONT_HERSHEY_PLAIN,0.8,(255,0,0),1)
    # if the blue in both sides is exists so will enter the if condtion 
    if(get_the_coutours(img1) and get_the_coutours(img2)):
        # object to detect the blue colour 
        Colourdetectio2=DetectColour(frame,lowerBlue,upperBlue,200) ##creat an object of the class)
        # get the countours of blue in frame 
        contours2=Colourdetectio2.getcontours(frame)
        # object to detect the brown colour 
        Colourdetectio3=DetectColour(frame,lowBrown,upperBrown,50) ##creat an object of the class)
        #  get the countnours of the brown in the frame
        contours3=Colourdetectio3.getcontours(frame)
        #  now will try to get two midpoint betwween the two blue lines and scale them into contanst measure distance 
        try:
            # Will get teh boundry of the first countour the first blue line and second one then get the midpoint between them and draw a line 
            x,y,w,h = cv2.boundingRect(contours2[0])
            x2,y2,w2,h2 = cv2.boundingRect(contours2[1])
            point1_x=x+w//2
            point2_x=x2+w2//2
            point1_y=y+h//2
            point2_y=y2+h2//2
            cv2.circle(frame,(x+w//2,y+h//2),10,(0,0,255),-1)
            cv2.circle(frame,(x2+w2//2,y2+h2//2),10,(0,0,255),-1)
            cv2.line(frame,(x+w//2,y+h//2),(x2+w2//2,y2+h2//2),(0,0,255),5)
            cv2.putText(frame,f"{round(compute_distance(x+w//2,y+h//2,x2+w2//2,y2+h2//2),2)}pix,20cm",((point2_x+point1_x)//2,(point2_y+point1_y)//2),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),1)
            # Compute the distance betweenn the two points 
            print(f"The distance between the two blue lines in pixels={compute_distance(x+w//2,y+h//2,x2+w2//2,y2+h2//2)} ")
            # This is the ration cm over the pixels u can use it to measure any thing in the frame 
            ratio=Distance_between_two_blue_line_in_cm/compute_distance(x+w//2,y+h//2,x2+w2//2,y2+h2//2)
            # Now will get the boundry box arounf the wreck and print on it's length in the pixels  
            x3,y3,w3,h3=cv2.boundingRect(contours3[0])
            cv2.rectangle(img2,(x3,y3),(x3+w3,y3+h3),(0,255,0),2)
            cv2.putText(frame,f"{round(compute_distance(x3,y3,x3,y3+h3),2)}pix",(10,50),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),1)
            # Print the length in cm after multiply it by ratio
            cv2.putText(frame,f"{round(round(compute_distance(x3,y3,x3,y3+h3),2)*ratio,2)}cm",(200,50),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),1)
   
        except:
            pass
    cv2.imshow("img1",img1)
    cv2.imshow("img2",img2)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()
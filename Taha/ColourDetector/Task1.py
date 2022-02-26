import cv2
import numpy as np
from ColourDetector import DetectColour
img = cv2.imread("bosla.jpg")
lower_red = np.array([159, 50, 70])  # range of the red colour
upper_red = np.array([180, 255, 255])  # range of the color
###################### Function to get the max and min for x and y form the countours ############################################


def get_list_values(contours):
    x = []
    y = []
    for i in list(contours):
        for j in i:
            for k in j:
                x.append(k[0])
                y.append(k[1])
    return [(max(x), y[x.index(max(x))]), (min(x), y[x.index(min(x))]), (x[y.index(max(y))], max(y)), (x[y.index(min(y))], min(y))]
############################################################### Get the countours from the colour dector class ############################


def get_the_coutours(img):
    # creat an object of the class)
    Colourdetectio = DetectColour(img, lower_red, upper_red, 800)
    contours = Colourdetectio.getcontours(img)
    imgmask = np.ones([img.shape[0], img.shape[1], 3], dtype=np.uint8)
    imgmask = cv2.drawContours(imgmask, contours, -1, (255, 255, 255), -1)
    # cv2.imshow("mask",imgmask)
    if len(contours) > 0:
        return True
    else:
        return False


##################################################### Here we inalized the used camera(take care to change it when use dvr) ##########################
cap = cv2.VideoCapture(0)
################################################################ Main loop #####################################################
# ############33
up_status = False
down_status = False
left_status = False
right_Status = True
end_status = False
counter = 0
enter = '5'
while True:
    ret, img = cap.read()
    try:
        h, w, c = img.shape
        w1 = w//3
        w2 = w*2//3
        h1 = h//3
        h2 = h*2//3
        # cv2.line(img,(w1,0),(w1,h),(255,255,255),0.5)
        # cv2.line(img,(w2,0),(w2,h),(255,255,255),0.5)
        # cv2.line(img,(0,h1),(w,h1),(255,255,255),0.5)
        # cv2.line(img,(0,h2),(w,h2),(255,255,255),0.5)
        img1 = img[:h1, :w1]
        img2 = img[:h1, w1:w2]
        img3 = img[:h1, w2:]
        img4 = img[h1:h2, :w1]
        img5 = img[h1:h2, w1:w2]
        img6 = img[h1:h2, w2:]
        img7 = img[h2:, :w1]
        img8 = img[h2:, w1:w2]
        img9 = img[h2:, w2:]
        cv2.imshow("img1", img1)
        cv2.imshow("img2", img2)
        cv2.imshow("img3", img3)
        cv2.imshow("img4", img4)
        cv2.imshow("img5", img5)
        cv2.imshow("img6", img6)
        cv2.imshow("img7", img7)
        cv2.imshow("img8", img8)
        cv2.imshow("img9", img9)
        c1 = get_the_coutours(img1)
        cv2.putText(img1, f"ContaingRed:{c1}", (20, 80),
                    cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
        c2 = get_the_coutours(img2)
        cv2.putText(img2, f"ContaingRed:{c2}", (20, 80),
                    cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
        c3 = get_the_coutours(img3)
        cv2.putText(img3, f"ContaingRed:{c3}", (20, 80),
                    cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
        c4 = get_the_coutours(img4)
        cv2.putText(img4, f"ContaingRed:{c4}", (20, 80),
                    cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
        c5 = get_the_coutours(img5)
        cv2.putText(img5, f"ContaingRed:{c5}", (20, 80),
                    cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
        c6 = get_the_coutours(img6)
        cv2.putText(img6, f"ContaingRed:{c6}", (20, 80),
                    cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
        c7 = get_the_coutours(img7)
        cv2.putText(img7, f"ContaingRed:{c7}", (20, 80),
                    cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
        c8 = get_the_coutours(img8)
        cv2.putText(img8, f"ContaingRed:{c8}", (20, 80),
                    cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
        c9 = get_the_coutours(img7)
        cv2.putText(img9, f"ContaingRed:{c9}", (20, 80),
                    cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)\

        if c4 and c5 and c6:
            if right_Status:
                cv2.putText(img, "Contaniue moveing to right", (10, 20),
                            cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 1)
            elif left_status:
                cv2.putText(img, "Contaniue moveing to Left", (10, 20),
                            cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 1)
                counter = 0
        if c2 and c5 and c8:
            cv2.putText(img, "Go to down", (10, 20),
                        cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 1)
            if counter == 0:
            
                right_Status = not(right_Status)
                left_status = not(left_status)
            counter += 1

        cv2.imshow("img", img)
    except:
        pass
# cv2.waitKey(0)
    if cv2.waitKey(1) == ord("q"):
        break

        # c1=get_the_coutours(img1)
        # c2=get_the_coutours(img2)
        # c3=get_the_coutours(img3)
        # c4=get_the_coutours(img4)
        # c5=get_the_coutours(img5)
        # c6=get_the_coutours(img6)
        # if not(c1) and c2 and c3:
        #     cv2.putText(img,"Move Right",(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),1)
        # if c2 and c3 and c6:
        #     cv2.putText(img,"Move Right then to down",(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),1)
        # if c6 and c5 and c4:
        #     cv2.putText(img,"Move to left",(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),1)
        #     left_status=False
        # if c4 and c1 and c2:
        #      cv2.putText(img,"Move to left then down",(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),1)
        #      left_status=True
        # if c4 and c5 and c6 and left_status:
        #     cv2.putText(img,"Move Right",(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),1)
        # if c5 and c6==False:
        #      cv2.putText(img,"End",(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),1)

    # max_x_point=get_list_values(get_the_coutours(img))[0]##get the max x point
    # min_x_point=get_list_values(get_the_coutours(img))[1]## get the min x point
    # max_y_point=get_list_values(get_the_coutours(img))[2]##get the max y point
    # min_y_point=get_list_values(get_the_coutours(img))[3]##get the min y point
    # ################################# Put the name of the point and point on the image #################################################
    # cv2.putText(img,"max_x",max_x_point,cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
    # cv2.putText(img,"min_x",min_x_point,cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
    # cv2.putText(img,"max_y",max_y_point,cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
    # cv2.putText(img,"min_y",min_y_point,cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
    # cv2.circle(img,max_x_point, 1, (0,0,255), -1)
    # cv2.circle(img,min_x_point, 1, (0,0,255), -1)
    # cv2.circle(img,max_y_point, 1, (0,0,255), -1)
    # cv2.circle(img,min_y_point, 1, (0,0,255), -1)
    # ############################################################### Match betwwen the points by line #############################
    # cv2.line(img,min_x_point,max_x_point,(255,0,255),2)
    # cv2.line(img,min_y_point,max_y_point,(255,225,0),2)
    ####################################################################################################################
    ############################# Unpacking each point to x and y to can maniuplate them ###############################
    # x1,y1=max_x_point
    # x2,y2=min_x_point
    # x3,y3=max_y_point
    # x4,y4=min_y_point
    # if x1>x2:
    #     if left_status==False and right_Status==False: ##intialstate
    #         cv2.putText(img,"Go To Right",(50,50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
    #         right_Status=True
    #     elif left_status==False and right_Status==True :
    #         if y4<y3:
    #             cv2.putText(img,"Go To right then to down",(50,50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
    #             right_Status=False
    #             down_status=True
    #             left_status=True
    #         else:
    #             cv2.putText(img,"Go To Right",(50,50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
    #             right_Status=True

    #     elif left_status==True and down_status==True:
    #         if x==1:
    #             cv2.putText(img,"Go down then to left",(50,50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
    #             down_status=False
    #         else:
    #             cv2.putText(img,"Go left then to down",(50,50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
    #             down_status=False
    #     elif left_status==True and right_Status==False and down_status==False:
    #         cv2.putText(img,"Continue to left",(50,50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
    #         down_status=True

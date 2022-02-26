import cv2
import numpy as np
from ColourDetector import DetectColour

lower_red = np.array([150, 50, 70])  # range of the red colour
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
    cv2.imshow("mask", imgmask)
    return contours


img = cv2.imread('bosla.jpg')


max_x_point = get_list_values(get_the_coutours(img))[
    0]  # get the max x point
min_x_point = get_list_values(get_the_coutours(img))[
    1]  # get the min x point
max_y_point = get_list_values(get_the_coutours(img))[
    2]  # get the max y point
min_y_point = get_list_values(get_the_coutours(img))[
    3]  # get the min y point
################################# Put the name of the point and point on the image #################################################
cv2.putText(img, "max_x", max_x_point,
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.putText(img, "min_x", min_x_point,
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.putText(img, "max_y", max_y_point,
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
cv2.putText(img, "min_y", min_y_point,
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
cv2.circle(img, max_x_point, 3, (0, 0, 255), -1)
cv2.circle(img, min_x_point, 3, (0, 0, 255), -1)
cv2.circle(img, max_y_point, 3, (0, 0, 255), -1)
cv2.circle(img, min_y_point, 3, (0, 0, 255), -1)
############################################################### Match betwwen the points by line #############################
cv2.line(img, min_x_point, max_x_point, (255, 0, 255), 2)
cv2.line(img, min_y_point, max_y_point, (255, 225, 0), 2)
####################################################################################################################
############################# Unpacking each point to x and y to can maniuplate them ###############################
x1, y1 = max_x_point
x2, y2 = min_x_point
x3, y3 = max_y_point
x4, y4 = min_y_point
if x1 > x2:
    cv2.putText(img, "toleft", (10, 10),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
elif x2 > x1:
    cv2.putText(img, "toRight", (10, 10),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    ##################################################################################################################

print("max", x1, y1)
print("min", x2, y2)
print("################")
cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

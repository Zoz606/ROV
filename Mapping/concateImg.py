import cv2 as cv

img1 = cv.imread('1.jpg')
img2 = cv.imread('2.jpg')

# vertically concatenates images
# of same width
im_v = cv.hconcat([img1, img1])

# show the output image
cv.imshow('sea_image.jpg', im_v)

cv.waitKey()
cv.destroyAllWindows()
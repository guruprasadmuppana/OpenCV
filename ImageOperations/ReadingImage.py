
import cv2
import numpy as np

file = "Images/rose-flower.jpg"

# Reading the image
img = cv2.imread(file)

# Displaying the image
cv2.imshow("Original",img)

# Saving the image into a new file
cv2.imwrite("Images/new-rose.jpg",img)

# resize the image
width = 500
height = 500
imgResize = cv2.resize(img,(width,height))
cv2.imshow(" resized flower",imgResize)

# resize using scale
scale=0.5
imgResize = cv2.resize(img, (0,0), None,scale, scale)
cv2.imshow(" resized 1",imgResize)


# X range and Y range goes into the original image
imgCropped = img[50:500,450:900]
cv2.imshow("cropped flower",imgCropped)
#
#
imgGray = cv2.cvtColor(imgCropped,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",imgGray)
#
imgNeg = cv2.bitwise_not(imgCropped)
cv2.imshow("Negative",imgNeg)
#

# Wait until any key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
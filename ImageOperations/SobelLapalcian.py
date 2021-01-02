import cv2
import numpy as np
import matplotlib.pyplot as plt

# file = "Images/Diamond-Jewelry.jpg"
file = "Images/saree.jpg"
# file = "Images/pages.jpeg"


# file = "Images/shapes.png"
# file = "images/colorBlocks.jpg"

# Reading the image
img = cv2.imread(file)
cv2.imshow("Original",img)
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Original Gray",imgGray) # using THRESH_TRUNC
imgGray = img


# img_sobel_x = cv2.Sobel(imgGray,cv2.CV_64F,1,0,ksize=3)
# img_sobel_y = cv2.Sobel(imgGray,cv2.CV_64F,0,1,ksize=3)
# cv2.imshow("Sobel X", np.absolute(img_sobel_x)) # absolute is used to avoid negative derivatives.
# cv2.imshow("Sobel Y", np.absolute(img_sobel_y))


# img_lap = cv2.Laplacian(imgGray,cv2.CV_64F,ksize=7, borderType=cv2.BORDER_DEFAULT)
# cv2.imshow("laplacian", cv2.cvtColor(img_lap,cv2.COLOR_BGR2GRAY))

img_lap = cv2.Laplacian(imgGray,cv2.CV_64F,ksize=3) # ksize=1 will work better
img_lap = np.uint8(np.absolute(img_lap))
cv2.imshow("laplacian", cv2.cvtColor(img_lap,cv2.COLOR_BGR2GRAY))

cv

# cv2.BORDER_WRAP
# cv2.BORDER_REFLECT
# cv2.BORDER_REFLECT101
# cv2.BORDER_REPLICATE
# cv2.BORDER_TRANSPARENT
# cv2.BORDER_CONSTANT
# cv2.BORDER_ISOLATED
# cv2.BORDER_REFLECT_101

# scharr_x = cv2.Scharr(imgGray, ddepth=-1, dx=1, dy=0, scale=1, borderType=cv2.BORDER_CONSTANT)
# cv2.imshow("Scharr X", np.absolute(scharr_x))
#
# scharr_y = cv2.Scharr(imgGray, ddepth=-1, dx=0, dy=1, scale=1, borderType=cv2.BORDER_DEFAULT)
# cv2.imshow("Scharr Y", np.absolute(scharr_y))
#
# scharr_filter = scharr_x + scharr_y
# cv2.imshow("Scharr Filter", scharr_filter)

# Wait until any key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()

# all parameters
# lap_filter = cv2.Laplacian(image, ddepth=-1, ksize=7, scale=1, borderType=cv2.BORDER_DEFAULT)
# cv2.imshow("Laplacian Filter", lap_filter)

# # Scharr High Pass Filter Implementation
# scharrx_filter = cv2.Scharr(image, ddepth=-1, dx=1, dy=0, scale=1, borderType=cv2.BORDER_DEFAULT)
# cv2.imshow("Scharr X Filter", scharrx_filter)
#
# scharry_filter = cv2.Scharr(image, ddepth=-1, dx=0, dy=1, scale=1, borderType=cv2.BORDER_DEFAULT)
# cv2.imshow("Scharr Y Filter", scharry_filter)
#
# scharr_filter = scharrx_filter + scharry_filter
# cv2.imshow("Scharr Filter", scharr_filter)


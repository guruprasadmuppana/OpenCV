
import cv2
import numpy as np
import matplotlib.pyplot as plt


file = "Images/rice.jpg"

# Reading the image
img = cv2.imread(file)

# converted into RGB colors
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# Grayscale = (R + G + B ) / 3
imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
imgGray_rgb = cv2.cvtColor(imgGray,cv2.COLOR_GRAY2RGB)

# thresholdVal = 90
# maxVal = 255
# retValue,imgThreshold = cv2.threshold(imgGray,thresholdVal,maxVal,cv2.THRESH_BINARY) # THRESH_TOZERO_INV
# imgThreshold_rgb = cv2.cvtColor(imgThreshold,cv2.COLOR_GRAY2RGB) # return value is not used
# cv2.imshow("thershold",imgThreshold_rgb)
#
#
# #adaptive threshold
# # takes in gray image only
# blockSize=11
# constantC=2
# imgAdaMean = cv2.adaptiveThreshold(imgGray,maxVal,cv2.ADAPTIVE_THRESH_MEAN_C,\
#             cv2.THRESH_BINARY,blockSize,constantC)
# imgAdaGaussian = cv2.adaptiveThreshold(imgGray,maxVal,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#             cv2.THRESH_BINARY,blockSize,constantC)
#
# cv2.imshow("adaptive mean",imgAdaMean)
# cv2.imshow("adaptive Gaussian",imgAdaGaussian)


# Binary Threshold in color.
img = cv2.imread("Images/temple.jpg")
cv2.imshow("original",img)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# threshold
bluemin = np.array([85, 60, 60], np.uint8)
bluemax = np.array([150, 255, 255], np.uint8)

red1min = np.array([0, 100, 100], np.uint8)
red1max = np.array([10, 255, 255], np.uint8)
red2min = np.array([160, 100, 100], np.uint8)
red2max = np.array([179, 255, 255], np.uint8)

mask = cv2.inRange(imgHSV, bluemin, bluemax) # identified colored areas are marked white and the rest as black
# cv2.imshow("mask",mask)

# mask = cv2.inRange(imgHSV, red1min, red1max)
# plt.imshow(mask)

mask_inv = cv2.bitwise_not(mask) # all colored areas become black
mask_inv_rgb = cv2.cvtColor(mask_inv, cv2.COLOR_GRAY2RGB)
# plt.imshow(mask_rgb)

# create masked image (overlap the mask on the original image
masked_img = cv2.bitwise_and(img, mask_inv_rgb)

# plt.imshow(masked_img)
# cv2.imshow("masked image",masked_img)

mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
merged_img = cv2.addWeighted(masked_img, 1,mask_rgb, 1, 0)

cv2.imshow("merged",merged_img)

# plt.imshow(cv2.cvtColor(merged_img, cv2.COLOR_BGR2RGB))

 # plt.show()



# Wait until any key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()



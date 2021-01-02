import cv2
import numpy as np

# Binary Threshold in color.
img = cv2.imread("Images/temple.jpg")
cv2.imshow("original",img)
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# threshold
bluemin = np.array([85, 60, 60], np.uint8)
bluemax = np.array([150, 255, 255], np.uint8)

mask = cv2.inRange(imgHSV, bluemin, bluemax) # identified colored areas are marked white and the rest as black
cv2.imshow("mask",mask)

mask_inv = cv2.bitwise_not(mask) # all colored areas become black
mask_inv_rgb = cv2.cvtColor(mask_inv, cv2.COLOR_GRAY2RGB)

# create masked image (overlap the mask on the original image
masked_img = cv2.bitwise_and(img, mask_inv_rgb)

cv2.imshow("masked image",masked_img)

mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
merged_img = cv2.addWeighted(masked_img, 1,mask_rgb, 1, 0)

cv2.imshow("merged- Image without background",merged_img)

# Wait until any key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()




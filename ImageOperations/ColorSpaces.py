import cv2
import numpy as np
import matplotlib.pyplot as plt


file = "images\sunflower.jpg"
img = cv2.imread(file)
# cv2.imshow("original", img)

#slice the colors:
print("Original Image ", img.shape)
# Open CV is BGR model
b,g,r = cv2.split(img)
print(b.shape,g.shape,r.shape)

# cv2.imshow("Blue",b)
# cv2.imshow("Green",g)
# cv2.imshow("Red",r)
#

# histogtrams
# plt.hist(b.ravel(), 256, [0, 256])
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])
# plt.show()

empty_img = np.zeros((img.shape[0],img.shape[1]),np.uint8)
# cv2.imshow("Empty Sheet",empty_img)
# print(empty_img.shape)
# Blue color using RGB
# blue_img = cv2.merge((b,empty_img,empty_img))
# cv2.imshow("Blue Sheet",blue_img)
# green_img = cv2.merge((empty_img,g,empty_img))
# cv2.imshow("Green Sheet",green_img)
# red_img = cv2.merge((empty_img,empty_img,r))
# cv2.imshow("Red Sheet",red_img)
# #
# cv2.imshow("Displaying Open CV - BGR ", img)
# rgb_img = cv2.merge((r,g,b))
# plt.imshow(rgb_img)
# plt.title("Displaying using Matplotlib - RGB")
# plt.show()
#
#
# Creating Gray Color using our own computation
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray-using ctv", imgGray)

gray_img = (r*0.3)+(g*.59)+(b*.11)
gray_img = gray_img.astype(np.uint8)
cv2.imshow("Gray image computed from Red, Green and Blue ",gray_img)


cv2.waitKey(0)
cv2.destroyAllWindows()

# notes
# green = np.uit8([[[0,255,0 ]]])
# hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
# print( hsv_green )
# [[[ 60 255 255]]]
# Now you take [H-10, 100,100] and [H+10, 255, 255]
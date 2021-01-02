import cv2
import numpy as np
#
# img = cv2.imread("images/coins-Marcel_strau_unsplash.jpg")
# # img = cv2.imread("images/coin_claudio_schwarz_unsplash.jpg")
# # img = cv2.imread("images/coins.jpg")
#
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # imgGrayBlur = cv2.GaussianBlur(imgGray, (3,3),0)
# # imgGrayBlur = cv2.adaptiveThreshold(imgGray, 150, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,0)
# imgGrayBlur = cv2.medianBlur(imgGray,5)
#
# cv2.imshow("img", imgGrayBlur)
#
# # imgCanny = cv2.Canny(imgGrayBlur,100,200)
# imgCanny = cv2.Canny(imgGrayBlur,180,255)
# cv2.imshow("canny", imgCanny)
#
# # circles_h = cv2.HoughCircles(imgGrayBlur,cv2.HOUGH_GRADIENT, 1.15, 10)
#
# # circles_h = cv2.HoughCircles(imgCanny,cv2.HOUGH_GRADIENT,1,10,
# #                            param1=180,param2=27,minRadius=20,maxRadius=60)
#
# circles_h = cv2.HoughCircles(imgGrayBlur,cv2.HOUGH_GRADIENT,1,10,
#                            param1=180,param2=27,minRadius=20,maxRadius=60)
#
#
# #circles is 3D data. but with only one item of circle
# if (circles_h is not None):
#     circles = circles_h[0]
#     circles  = np.uint16(np.around(circles))
#     for cir in circles:
#         cv2.circle(img,(cir[0],cir[1]),cir[2], (0,0,255),3)
#     print(type(circles))
#     print(circles)
#
# cv2.imshow("detected circles", img)

###################
# # Read image
img = cv2.imread("images/Sunflowers.jpg")
# img = cv2.imread("images/flowers.jpg")
# img = cv2.imread("images/flowerpots.jpg")
# img = cv2.imread("images/nightsky.jpg")
img = cv2.imread("images/stars.jpg")


# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create()


# Detect blobs.
keypoints = detector.detect(img)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of
# the circle corresponds to the size of blob
blank = np.zeros((1, 1))
# blank = np.zeros((5, 5))
blobs = cv2.drawKeypoints(img, keypoints, blank, (0, 0, 255),
                          cv2.DrawMatchesFlags_DEFAULT)
#.DRAW_MATCHES_FLAGS_DEFAULT
print(len(blobs))

cv2.imshow("Blobs", blobs)

cv2.waitKey(0)
cv2.destroyAllWindows()


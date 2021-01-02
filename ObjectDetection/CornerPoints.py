import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
        Harris Corner Detector
        ----------------------
1.) Determine which windows produce very large
    variations in intensity when moved in both 
    X and Y directions.
2.) With each such window found, a score R is
    computed.
3.) After applying a threshold to this score,
    important corners are selected & marked.
'''

file = "images/shapes.png"
# # file = "images/temple.jpg"
# file = "images/window1.jpg"
imggray = cv2.imread(file,cv2.IMREAD_GRAYSCALE)
# cv2.imshow("shapes original",imggray)

'''
img - Input image, it should be grayscale and float32 type.
blockSize - It is the size of neighbourhood considered for corner detection
ksize - Aperture parameter of Sobel derivative used.
k - Harris detector free parameter in the equation.
'''

# find Harris corners
gray = np.float32(imggray)
dst = cv2.cornerHarris(gray,2,3,0.04)

dst = cv2.dilate(dst,None)
threshold = 0.01*dst.max()
ret, dst = cv2.threshold(dst,threshold,255,0)
dst = np.uint8(dst)
# print(dst)
cv2.imshow("shapes",dst)
#

# # goodFeaturesToTrack: shiThomasi
#
# file = "images/shapes.png"
# # # file = "images/temple.jpg"
# # file = "images/window1.jpg"
#
# gray = cv2.imread(file, 0)
# # cv2.imshow('cornors:goodFeaturesToTrack', gray)
#
# img = np.zeros((gray.shape[0],gray.shape[1],3),np.uint8)
# corners = cv2.goodFeaturesToTrack(gray, 20, 0.05, 50)
#
# print(type(corners))
# print(corners)
# # corners = np.int0(corners)
#
# for i in corners:
#     # x, y = i.ravel()
#     x, y = i[0]
#     x = int(x)
#     y = int(y)
#     cv2.circle(gray, (x, y), 3, (0, 255, 0), -1)
#     cv2.circle(img, (x, y), 3, (0, 255, 0), -1)
#
# cv2.imshow('cornors:goodFeaturesToTrack', gray)
# cv2.imshow('cornors on blank', img)


# ORB Oriented Fast and Rotated BRIEF
#
# file = "images/shapes.png"
# file = "images/temple.jpg"
# # file = "images/window1.jpg"
#
# image = cv2.imread(file)
# gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# img = np.zeros((gray.shape[0],gray.shape[1],3),np.uint8)
#
# print("starting ORB")
#
# # 1000 is the max key points we like to identify
# # orb = cv2.ORB(5000)
# orb = cv2.ORB(1000,1.2)
#
# keypoints = orb.detect(gray,None)
#
# print("starting ORB111")
#
# keypoints, descriptors = orb.compute(gray,keypoints)
# print("Number of keypoints", len(keypoints))
#
#
# # draw the keypoints
# # image = cv2.drawKeypoints(gray,keypoints,flag=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
# image =  cv2.drawKeypoints(image,keypoints,flag=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# # cv2.drawKeypoints(img,keypoints,flag=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#
#
# cv2.imshow('cornors:ORB', image)
# # cv2.imshow('cornors on blank', img)
#

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

# read image and show
file = "images/colorBlocks.jpg"
file = "images/graph.png"
file = "images/window1.jpg"

img = cv2.imread(file)

# cv2.imshow("original",img)

#gray 
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgCanny = cv2.Canny(imgGray,100,200,apertureSize=3)

lines = cv2.HoughLines(imgCanny,1, np.pi/180,240)
print("lines", len(lines))

linesP = cv2.HoughLinesP(imgCanny,1, np.pi/180,50,50,10) # min len = 5, max gap = 10
print("linesP", len(linesP))
# print(linesP)

# for lineP in linesP:
#     # print(line)
#     for l in lineP:
#         # x1,y1 , x2, y2 = l
#         # cv2.line(img,(x1,y1),(x2, y2), (255, 255,0), 1)
#         cv2.imshow("original", img)
#

# for line in lines:
#     for p, angle in line:
#         # print(p, angle)
#         a = np.cos(angle)
#         b = np.sin(angle)
#         x0 = a * p
#         y0 = b * p
#         constant = p
#         x1 = int(x0 + constant * (-b))
#         y1 = int(y0 + constant * (a))
#         x2 = int(x0 - constant * (-b))
#         y2 = int(y0 - constant * (a))
#         print((x1, y1), (x2, y2))
#         cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# identifying circles

# image = cv2.imread("images/concentratic_circles.jpg")
# image = cv2.imread("images/circle.jpg")
#
#
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # blur = cv2.GaussianBlur(gray,(5,5),0)
#
# blur = cv2.medianBlur(gray, 5)
# circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.5, 20,minRadius=0,maxRadius=0)
#
# # circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,20,
# #                             param1=50,param2=30,minRadius=50,maxRadius=500)
# print(len(circles[0]))
# circles = np.uint16(np.around(circles))
#
# for i in circles[0, :]:
#     # draw the outer circle
#     print(i)
#     # i = i.astype(np.uint8)
#     cv2.circle(image, (i[0], i[1]), i[2], (255, 0, 0), 2)
#
#     # draw the center of the circle
#     cv2.circle(image, (i[0], i[1]), 2, (0, 255, 0), 5)
#
# # cv2.imshow("circles",image)


### second attempt
'''
(x-xc)^2 + (y-yc)^2 = r^2   
#Formula of circle
'''
img = cv2.imread('images/circle.jpg')
img = cv2.imread('images/coins.jpg')
img = cv2.resize(img, (700, 400))
output = img.copy()
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray_img, 5)
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT,
                          1, 100, 10, param1=130, param2=55, minRadius=5, maxRadius=0)
# circles = cv.HoughCircles(blur, cv.HOUGH_GRADIENT,
#                           1, 10)
detected_circles = np.uint16(np.around(circles))

for (x, y, r) in detected_circles[0, :]:
    cv2.circle(output, (x, y), r, (0, 255, 0), 3)
    cv2.circle(output, (x, y), 2, (255, 0, 0), 3)

cv2.imshow("Original Image", img)
cv2.imshow("Output", output)




# Detecting blobs

#
# stars = cv2.imread("images/stars.jpg")
# stars = cv2.cvtColor(stars,cv2.COLOR_BGR2GRAY)
# # cv2.imshow("stars",stars)
#
# detector = cv2.SimpleBlobDetector()
# print(detector)
#
# keypoints = detector.detect(stars)
# print("keypoints",keypoints)
# blank = np.zeros((1,1))
#
# blobs = cv2.drawKeypoints(stars, keypoints, blank, (0,255,255), cv2.DRAW_MATCHES_FLAGS_DEFAULT)
# # print("blobs",blobs)
# # cv2.imshow("Blobs",blobs)
# cv2.imshow("stars",stars)
#

cv2.waitKey(0)
cv2.destroyAllWindows()



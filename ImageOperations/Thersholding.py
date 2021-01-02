
import cv2
import numpy as np
import matplotlib.pyplot as plt

size = 256
img = np.zeros((size,size),np.uint8)
# cv2.imshow("reference img",img.copy())

for i in range(256):
    img[i:]=i
cv2.imshow("gradient img",img)

#Trackbar creation using four step method.
trackbarName = 'ThersholdTracker'
cv2.namedWindow(trackbarName)
def callback(x):
    pass
cv2.createTrackbar("Threshold Value",trackbarName, 50, 255, callback)

while True:
    imgGray = img.copy()
    thresholdVal = cv2.getTrackbarPos("Threshold Value",trackbarName)
    print(thresholdVal)
    maxVal = 255
    retValue,imgThreshold_THRESH_BINARY = cv2.threshold(imgGray,thresholdVal,maxVal,cv2.THRESH_BINARY)
    imgThreshold_THRESH_BINARY = cv2.line(cv2.cvtColor(imgThreshold_THRESH_BINARY,cv2.COLOR_GRAY2BGR),
                                          (0,thresholdVal),(255,thresholdVal),(0,0,255),2)


    retValue, imgThreshold_THRESH_BINARY_INV = cv2.threshold(imgGray, thresholdVal, maxVal, cv2.THRESH_BINARY_INV)
    imgThreshold_THRESH_BINARY_INV = cv2.line(cv2.cvtColor(imgThreshold_THRESH_BINARY_INV, cv2.COLOR_GRAY2BGR),
                                          (0, thresholdVal), (255, thresholdVal), (0, 0, 255), 2)

    retValue,imgThreshold_THRESH_TOZERO = cv2.threshold(imgGray,thresholdVal,maxVal,cv2.THRESH_TOZERO)
    imgThreshold_THRESH_TOZERO = cv2.line(cv2.cvtColor(imgThreshold_THRESH_TOZERO, cv2.COLOR_GRAY2BGR),
                                          (0, thresholdVal), (255, thresholdVal), (0, 0, 255), 2)

    retValue,imgThreshold_THRESH_TOZERO_INV = cv2.threshold(imgGray,thresholdVal,maxVal,cv2.THRESH_TOZERO_INV)
    imgThreshold_THRESH_TOZERO_INV = cv2.line(cv2.cvtColor(imgThreshold_THRESH_TOZERO_INV, cv2.COLOR_GRAY2BGR),
                                          (0, thresholdVal), (255, thresholdVal), (0, 0, 255), 2)


    retValue,imgThreshold_THRESH_TRUNC = cv2.threshold(imgGray,thresholdVal,maxVal,cv2.THRESH_TRUNC)
    imgThreshold_THRESH_TRUNC = cv2.line(cv2.cvtColor(imgThreshold_THRESH_TRUNC, cv2.COLOR_GRAY2BGR),
                                          (0, thresholdVal), (255, thresholdVal), (0, 0, 255), 2)


    imgGradient = cv2.line(cv2.cvtColor(imgGray, cv2.COLOR_GRAY2BGR),
                                         (0, thresholdVal), (255, thresholdVal), (0, 0, 255), 2)

    cv2.imshow("BINARY",imgThreshold_THRESH_BINARY)
    cv2.imshow("BINARY_INV", imgThreshold_THRESH_BINARY_INV)
    cv2.imshow("TOZERO", imgThreshold_THRESH_TOZERO)
    cv2.imshow("TOZERO_INV", imgThreshold_THRESH_TOZERO_INV)
    cv2.imshow("TRUNC", imgThreshold_THRESH_TRUNC)
    cv2.imshow("gradient img", imgGradient)


    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # esc key
        break


# A demo using threshold on an image at the global level using the track bar
#
# file = "Images/park.jpg"
# # Reading the image
# img = cv2.imread(file)
# # cv2.imshow("Original",img)
# img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Original Gray",img) # using THRESH_TRUNC
#
# while True:
#     imgGray = img.copy()
#     thresholdVal = cv2.getTrackbarPos("Threshold Value",trackbarName)
#     print(thresholdVal)
#     maxVal = 255
#     retValue,imgThreshold_THRESH_BINARY = cv2.threshold(imgGray,thresholdVal,maxVal,cv2.THRESH_BINARY) #THRESH_TRUNC
#
#     cv2.imshow("Image ",imgThreshold_THRESH_BINARY)
#
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:  # esc key
#         break


# #
# # Adapative thereshold using mean and gaussian modes. It is blocked based thersholding.
# # it is good for gradiant color changes in the background.
# # The idea is to identify the edges of th shape.
#
#
# file = "Images/Diamond-Jewelry.jpg"
# file = "Images/saree.jpg"
# # file = "Images/bangles1.jpg"
# file = "Images/pages.jpeg"
# # file = "Images/shapes.png"
#
# # Reading the image
# img = cv2.imread(file)
# cv2.imshow("Original",img)
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Original Gray",imgGray) # using THRESH_TRUNC
#
# thresholdVal = 90
# maxVal = 255
# retValue,imgThreshold = cv2.threshold(imgGray,thresholdVal,maxVal,cv2.THRESH_BINARY)
# # cv2.imshow("thershold",imgThreshold)
#
# #adaptive threshold
# # takes in gray image only
# blockSize=5
# constantC=15
# imgAdaMean = cv2.adaptiveThreshold(imgGray,maxVal,cv2.ADAPTIVE_THRESH_MEAN_C,\
#             cv2.THRESH_BINARY,blockSize,constantC)
# imgAdaGaussian = cv2.adaptiveThreshold(imgGray,maxVal,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#             cv2.THRESH_BINARY,blockSize,constantC)
#
# cv2.imshow("adaptive mean",imgAdaMean)
# cv2.imshow("adaptive Gaussian",imgAdaGaussian)
#


# # OTUS automatic calculation for threshold for global value.
#
# #OTUS :
# file = "Images/Diamond-Jewelry.jpg"
# file = "Images/saree.jpg"
# file = "Images/gandhi.jpg"
# img = cv2.imread(file)
# img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# thershold = 60
# ret1,img_threshold = cv2.threshold(img,thershold,255,cv2.THRESH_BINARY)
# ret2,img_OTUS = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# cv2.imshow("Global Threshold",img_threshold)
# cv2.imshow("Otsu's Threshold",img_OTUS)
#
# plt.hist(img.ravel(), 256)
# plt.show()

# Wait until any key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()



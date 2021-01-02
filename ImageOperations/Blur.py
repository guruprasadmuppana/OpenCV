import cv2
import numpy as np

file = "Images/hair.jpg"

# Reading the image
img = cv2.imread(file)
# Displaying the image
cv2.imshow("original",img)

# blur = cv2.blur(img, (7,7))
# cv2.imshow('Blur', blur)
# #
# imgGaussianBlur = cv2.GaussianBlur(img,(7,7),0) # odd numbers for kernel
# cv2.imshow("GaussianBlur",imgGaussianBlur)
#
# median = cv2.medianBlur(img, 7)
# cv2.imshow('Median Blurring', median)
#
# bilateral = cv2.bilateralFilter(img, 5, 75, 75) # 95,95
# cv2.imshow('Bilateral Blurring', bilateral)

#
# # Custom filers
# # 3x3 filter
# blur_filter3x3 = np.ones((3, 3), np.float) / (9.0)
# # 5x5 filter
# blur_filter5x5 = np.ones((5, 5), np.float) / (25.0)
# # 7x7 filter
# blur_filter7x7 = np.ones((7, 7), np.float) / (49.0)
# #
# image_blur3x3 = cv2.filter2D(img, -1, blur_filter3x3)
# image_blur5x5 = cv2.filter2D(img, -1, blur_filter5x5)
# image_blur7x7 = cv2.filter2D(img, -1, blur_filter7x7)
#
# cv2.imshow('blur3x3', image_blur3x3)
# cv2.imshow('blur5x5', image_blur5x5)
# cv2.imshow('blur7x7', image_blur7x7)

#
# blur_filter5x5 = np.ones((5, 5), np.float) / (25.0)
# image_blur5x5 = cv2.filter2D(img, -1, blur_filter5x5)
# blur = cv2.blur(img, (5,5))
# cv2.imshow('blur from CV2', blur)
# cv2.imshow('custom filter ', image_blur5x5)


#Sharpening
sharpenignfilter = np.array( [
    [-1,-1,-1],
    [-1,9,-1],
    [-1,-1,-1]
])
image_sharpening = cv2.filter2D(img, -1, sharpenignfilter)
cv2.imshow('Sharpening', image_sharpening)



# non-local means of de-noising . non-local means filter takes into account of all pixel of the image
# instead of local (kernel) area alone.
imgNonLocalMeans = cv2.fastNlMeansDenoisingColored(img, None, 6,6,7,21)
imgNonLocalMeans = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)
# imgNonLocalMeans = cv2.fastNlMeansDenoisingColored(img, None, 20, 20, 7, 15)
cv2.imshow("Non-local means of denosing", imgNonLocalMeans)

# with gray color images.
imgGray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgNonLocalMeansGray = cv2.fastNlMeansDenoising(imgGray, None, 10, 10)
cv2.imshow("gray non-local",imgNonLocalMeansGray)


# Wait until any key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()








# file = "Images/Sunflower.jpg"
# file = "Images/Sunflower-medium.jpg"


#
#
# filter = np.array( [
#     [1,1,1],
#     [1,15,1],
#     [1,1,1]
# ])
# blur_filterCustom = filter/ (23.0)
# image_custom = cv2.filter2D(img, -1, blur_filterCustom)
# cv2.imshow('Custom', image_custom)
#


def mid(img):
    imgInfo = img.shape
    height = imgInfo[0]
    width = imgInfo[1]
    dst = np.empty_like(img, dtype=np.uint8)
    for i in range(height - 2):
        for j in range(width - 2):
            for channel in range(3):
                tmp = img[i:i+3, j:j+3, channel].reshape(1,9)
                dst[i,j, channel] = np.sort(tmp)[0,4]
    return dst

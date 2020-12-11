
import cv2
import numpy as np
import matplotlib.pyplot as plt

#Salt and Pepper noise
def saltandpepper(img,snr):
    h=img.shape[0]
    w=img.shape[1]
    imgDest=img.copy()
    sp=h*w
    NP=int(sp*(1-snr))
    for i in range (NP):
        randx=np.random.randint(1,h-1)   # random
        randy=np.random.randint(1,w-1)
        if np.random.random()<=0.5:
            imgDest[randx,randy]=0
        else:
            imgDest[randx,randy]=255
    return imgDest


file = "Images/Sunflower.jpg"


# Reading the image
img = cv2.imread(file)

# Displaying the image
cv2.imshow("original",img)

# 3x3 filter
blur_filter3x3 = np.ones((3, 3), np.float) / (9.0)
print(blur_filter3x3)

filter = np.array( [
    [-1,-1,-1],
    [-1,20,-1],
    [-1,-1,-1]
])

# filter = np.array( [
#     [1,1,1],
#     [1,15,1],
#     [1,1,1]
# ])
blur_filterCustom = filter/ (16.0)
print(blur_filterCustom)

# # 5x5 filter
# blur_filter5x5 = np.ones((5, 5), np.float) / (25.0)
# # 7x7 filter
# blur_filter7x7 = np.ones((7, 7), np.float) / (49.0)

image_blur3x3 = cv2.filter2D(img, -1, blur_filterCustom)
# image_blur5x5 = cv2.filter2D(img, -1, blur_filter5x5)
# image_blur7x7 = cv2.filter2D(img, -1, blur_filter7x7)

# cv2.imshow('blur3x3', image_blur3x3)
# cv2.imshow('blur5x5', image_blur5x5)
# cv2.imshow('blur7x7', image_blur7x7)


blur = cv2.blur(img, (3,3))
cv2.imshow('Blur', blur)

imgGaussianBlur = cv2.GaussianBlur(img,(7,7),0) # odd numbers for kernel
cv2.imshow("GaussianBlur",imgGaussianBlur)


imgslat = saltandpepper(img, 0.8)
cv2.imshow("salt and pepper",imgslat)

median = cv2.medianBlur(img, 5)
cv2.imshow('Median Blurring', median)

bilateral = cv2.bilateralFilter(img, 9, 95, 95)
cv2.imshow('Bilateral Blurring', bilateral)


merged_img = cv2.addWeighted(img, 0.5,image_blur3x3, 0.5, 0)
cv2.imshow('merged_img', merged_img)



# Wait until any key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()



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

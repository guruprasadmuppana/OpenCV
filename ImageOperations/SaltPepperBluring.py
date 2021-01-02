
import cv2
import numpy as np

#Salt and Pepper noise
def saltandpepper(img,snr):
    h=img.shape[0]
    w=img.shape[1]
    imgDest=img.copy()
    sp=h*w
    NP=int(sp*(1-snr))
    for i in range (NP):
        randx=np.random.randint(1,h-1)
        randy=np.random.randint(1,w-1)
        if np.random.random()<=0.5:
            imgDest[randx,randy]=0
        else:
            imgDest[randx,randy]=255
    return imgDest

file = "Images/gandhi.jpg"
# file = "Images/hair1.jpg"

# Reading the image
img = cv2.imread(file)
# Displaying the image
cv2.imshow("original",img)

imgslat = saltandpepper(img, 0.8)
cv2.imshow("salt and pepper",imgslat)

median = cv2.medianBlur(imgslat,5)
cv2.imshow('Median Blurring', median)


# Wait until any key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()



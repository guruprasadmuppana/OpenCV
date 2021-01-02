import cv2
import numpy as np


kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))

fgbg = cv2.createBackgroundSubtractorKNN()

cap = cv2.VideoCapture(0)
while (True):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    # fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN,kernel)
    # fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE,kernel)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CROSS, kernel)

    kernel = np.ones((5,5),np.uint8)

    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    fgmask = cv2.dilate(fgmask,kernel,iterations=1)

    contours, hierarchy = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    if contours is not None:
        contours = sorted(contours, key=cv2.contourArea,reverse=True)
        # cnts = sorted(contours, key=cv2.contourArea, reverse=True)
        cntmax = contours[0]
        cv2.drawContours(frame,contours,-1, (0,0,255),3)
        cv2.imshow("contours ", frame)

    # fgmask = cv2.erode(fgmask, kernel, iterations=2)
    # cv2.imshow("contours ", frame)
    cv2.imshow("background removal", fgmask)
    k = cv2.waitKey(1)
    if k == 13 : # enter key
        break

cap.release()
cv2.destroyAllWindows()


# ## applying this concept only to one image
# it shows only white screen. not sure if it works only substraction of consequente images
# image = cv2.imread("images/shivu.jpg")
# fgmask = fgbg.apply(image)
# fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CROSS, kernel)
# cv2.imshow("background removal", fgmask)
# k = cv2.waitKey(0)
# cv2.destroyAllWindows()


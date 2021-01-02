import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

# setup a location window
r,h,c,w = 250,100, 200,150
# r,h,c,w = 10,100, 10,150
track_window = (r,h,c,w)
# crop the region of interest (roi) from the image

roi_image = frame[r:r+h,c:c+w]

# convert the cropped image into HSV
roi_image_hsv = cv2.cvtColor(roi_image,cv2.COLOR_BGR2HSV)

#creat a mask for a specific color range.
red1min = np.array([0, 100, 100], np.uint8)
red1max = np.array([10, 255, 255], np.uint8)
red2min = np.array([160, 100, 100], np.uint8)
red2min = np.array([179, 255, 255], np.uint8)
red1_block_mask = cv2.inRange(roi_image_hsv,red1min,red1max)
red2_block_mask = cv2.inRange(roi_image_hsv,red2min,red2min)
red_block_mask = cv2.bitwise_or(red1_block_mask,red2_block_mask)
# red_areas = cv2.bitwise_and(imgColors,imgColors,mask=red_block_mask )

# obtain the color histogram of ROI

roi_hist = cv2.calcHist([roi_image_hsv],[0],red_block_mask,[180],[0,180])
print(roi_hist.shape)

# normalize teh value between 0 and 255
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

# setup a stop criteria
term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,1)

while (True):
    ret, frame = cap.read()
    if ret == True:
        # convert the image into HSV
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        # calculate histogram back projection
        dst = cv2.calcBackProject([hsv],[0],roi_hist, [0,180], 1)
        # print(dst.shape)

        # get the new location based on the mean shift
        ret, track_window = cv2.meanShift(dst,track_window, term_criteria)
        # draw it on the image:
        (x,y,w,h) = track_window
        image2 = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow("Mean shift tracking",image2)
        if cv2.waitKey(1) == 13 :
            break
    else:
        break



cap.release()
cv2.destroyAllWindows()

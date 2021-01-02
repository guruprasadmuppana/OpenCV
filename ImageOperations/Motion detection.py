
import cv2
import numpy as np

# vidio_file = "images/vtest.avi"
#
# cap = cv2.VideoCapture(vidio_file)
#
# cap = cv2.VideoCapture(0)
#
# _, frame1 = cap.read()
# _, frame2 = cap.read()
#
# while True:
#     diff = cv2.absdiff(frame1, frame2)
#     # cv2.imshow("video", diff)
#     # gray it
#     diff_gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
#     # blur using gaussian noise
#     smooth_diff = cv2.GaussianBlur(diff_gray,(5,5),0)
#     # cv2.imshow("video", smooth_diff)
#
#     _, frame_threshold = cv2.threshold(smooth_diff, 20, 255, cv2.THRESH_BINARY)
#     # cv2.imshow("video", frame_threshold)
#
#     dilated = cv2.dilate(frame_threshold, None, iterations=3)
#     # cv2.imshow("video", dilated)
#
#     # finding coutours
#     contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
#     cv2.drawContours(frame1, contours, -1, (0, 255, 0), 1) # -1 all
#
#     # for contour in contours:
#     #     (x, y, w, h) = cv2.boundingRect(contour)
#     #     if cv2.contourArea(contour) < 900:
#     #         continue
#     #     cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
#     #     # cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
#     #     #            1, (255, 0, 0), 3)
#
#     cv2.imshow("Video", frame1)
#     frame1 = frame2 #
#     ret, frame2 = cap.read()
#
#     k = cv2.waitKey(1)
#     if k == 27:
#         break


###############

cap = cv2.VideoCapture('images/vtest.avi')

cap = cv2.VideoCapture(0)


# fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=False)

while cap.isOpened():
    ret, frame = cap.read()
    if frame is None:
        break

    fgmask = fgbg.apply(frame)

    cv2.imshow('Frame', frame)
    cv2.imshow('FG Mask', fgmask)
    k = cv2.waitKey(1)
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()

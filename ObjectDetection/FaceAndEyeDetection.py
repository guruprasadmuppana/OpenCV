import cv2
import numpy as np

# face_classifier = cv2.CascadeClassifier("Classifiers/haarcascade_frontalface_default.xml")
# eye_classifier = cv2.CascadeClassifier("Classifiers/eye_detection.xml")
#
#
# def faceAndEyeDetection(img):
#     # use classifier to detection face first and then identify the eyes within the face area.
#     imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_classifier.detectMultiScale(imgGray,
#                                              1.05, # scaling while detecting with different sizes. it scale by 30%
#                                              5) # try different values. it is neighbourhood. valid values: 3 to 6
#     if faces == (): # if no faces are found, return the same image
#         return img
#     #get the bounded rectangle around the face. We will use some boarder to frame the face.
#     boarderSize = 1
#     for face in faces:
#         (x,y,w,h ) = face
#         cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
#         # extract the face area with borders.
#
#         # x -=boarderSize
#         # y -=boarderSize
#         # w +=boarderSize
#         # h +=boarderSize
#
#         x = x - boarderSize
#         w = w + boarderSize
#         y = y - boarderSize
#         h = h + boarderSize
#
#         roi_gray = imgGray[y:y+h,x:x+w] # y - item is in the first
#         roi_img =       img[y:y+h,x:x+w] # y - item is in the first
#         eyes = eye_classifier.detectMultiScale(roi_gray)
#         if eyes == ():
#             continue
#         else:
#             for eye in eyes:
#                 (ex, ey, ew,eh) = eye
#                 cv2.rectangle(roi_img, (ex,ey), (ex+ew, ey+eh), (0,255,0),2)
#                 roi_img = cv2.flip(roi_img, 1)
#
#     return img
#
#
# img = cv2.imread("images/daddy.jpg")
# img = cv2.imread("images/Shivanshu_face.jpg")
# img = cv2.imread("images/shivu.jpg")
# imgFace = faceAndEyeDetection(img)
# cv2.imshow("face detection", imgFace)
#
# #
# # cap = cv2.VideoCapture(0) # defect webcam
# # while (True):
# #     _, frame = cap.read()
# #     cv2.imshow("Face and Eye detection", faceAndEyeDetection(frame))
# #     k = cv2.waitKey(1)
# #     if k == 13 : # when enter key is pressed.
# #         break

#
# # 2. Full body detection:
# fullbody_classifier = cv2.CascadeClassifier("Classifiers/haarcascade_fullbody.xml")
# cap = cv2.VideoCapture("images/walking.avi")
#
# while (True):
#
#     _, frame = cap.read()
#     imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     fullbodies = fullbody_classifier.detectMultiScale(imgGray,
#                                              1.2, # scaling while detecting with different sizes. it scale by 30%
#                                              5) # try different values. it is neighbourhood. valid values: 3 to 6
#     for fullbody in fullbodies:
#         (x,y,w,h ) = fullbody
#         cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)
#
#     cv2.imshow("people walking", frame)
#     k = cv2.waitKey(1)
#     if k == 13 : # when enter key is pressed.
#         break
#

# 3. Car detectionS

car_classifier = cv2.CascadeClassifier("Classifiers/haarcascade_car.xml")
cap = cv2.VideoCapture("images/cars.avi")

while (True):

    _, frame = cap.read()
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_classifier.detectMultiScale(imgGray,
                                             1.2, # scaling while detecting with different sizes. it scale by 30%
                                             5) # try different values. it is neighbourhood. valid values: 3 to 6
    for car in cars:
        (x,y,w,h ) = car
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)

    cv2.imshow("cars", frame)
    k = cv2.waitKey(1)
    if k == 13 : # when enter key is pressed.
        break


cv2.waitKey(0)
cv2.destroyAllWindows()
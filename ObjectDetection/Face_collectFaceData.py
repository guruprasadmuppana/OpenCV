import cv2
import numpy as np


# collect the images from webcam and crop the images into 200x200 size
# store them in a directory called images/guru with index number.

# we will use face cascade classifier

face_classifier = cv2.CascadeClassifier("Classifiers/haarcascade_frontalface_default.xml")

# the above classifier will be used for detecting multiple scalled faces.

# let us capture the faces from webcam now

cap = cv2.VideoCapture(0) # 0 for default webcam

# let collect 100 images
count = 0
# path for storing the images:
data_path = "images/guru/"

def collect_face(frame):
    frameGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    facesRect = face_classifier.detectMultiScale(frameGray,1.3,5)
    if facesRect is ():
        print("no face found")
        return None
    for (x,y,w,h) in facesRect:
        roi = frameGray[y:y+h,x:x+w]
        # display the image collection progress by showing the face count.
        # cv2.putText(face,"Face: "+ str(count),(50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0),2)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(123,123,0),3)
        cv2.imshow("Face found",frame)

    return roi # if we find multiple faces, the last face will be returned.

while (True):
    ret, frame = cap.read()
    print(count)
    # process the image
    face = collect_face(frame)
    if face is not None:
        count +=1
        # resize the image to 200x200
        face = cv2.resize(face,(200,200))
        file_name = data_path + str(count) + '.jpg'
        print(file_name)
        cv2.imwrite(file_name, face)
        # # display the image collection progress by showing the face count.
        # cv2.putText(face,"Face: "+ str(count),(50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0),2)
        # cv2.imshow("Face found",face)

    if (count > 199) :
        break
    k = cv2.waitKey(1)
    if k == 13 : # enter key ; 27 for escape key
        break

cap.release()
cv2.destroyAllWindows()






# import cv2
# import numpy as np
#
# # Load HAAR face classifier
# face_classifier = cv2.CascadeClassifier('Classifiers/haarcascade_frontalface_default.xml')
#
#
# # Load functions
# def face_extractor(img):
#     # Function detects faces and returns the cropped face
#     # If no face detected, it returns the input image
#
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_classifier.detectMultiScale(gray, 1.3, 5)
#
#     if faces is ():
#         return None
#
#     # Crop all faces found
#     for (x, y, w, h) in faces:
#         cropped_face = img[y:y + h, x:x + w]
#
#     return cropped_face
#
#
# # Initialize Webcam
# cap = cv2.VideoCapture(0)
# count = 0
#
# # Collect 100 samples of your face from webcam input
# while True:
#
#     ret, frame = cap.read()
#     if face_extractor(frame) is not None:
#         count += 1
#         face = cv2.resize(face_extractor(frame), (200, 200))
#         face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
#
#         # Save file in specified directory with unique name
#         file_name_path = 'images/guru/' + str(count) + '.jpg'
#         cv2.imwrite(file_name_path, face)
#
#         # Put count on images and display live count
#         cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
#         cv2.imshow('Face Cropper', face)
#
#     else:
#         print("Face not found")
#         pass
#
#     if cv2.waitKey(1) == 13 or count == 100:  # 13 is the Enter Key
#         break
#
# cap.release()
# cv2.destroyAllWindows()
# print("Collecting Samples Complete")
#

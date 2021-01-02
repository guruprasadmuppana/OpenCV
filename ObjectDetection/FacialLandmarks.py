import cv2
import numpy as np

# for facial landmarks, we will use dLib library.
# dlib is C++ library
# one can download the library from here : https://sourceforge.net/projects/dclib/
# installation of dlib: Wheh you try to install using Pycharm -> files setting - Install library it failed.
# error: you right python file. It sounded like the path is not correct.

# install can be done using the following command:
# Use command prompt to Cd to folder and run “python setup.py install”

# above installation command failed.

# 2. i am downloading the cmake tool from https://cmake.org/ latest version 3.19.2 as on 28th dec 2020
# downloading cmake-3.19.2-win64-x64.msi file directly.
# while install ensure that cmake is part of PATH environment variable. Select that option during the installation.
#  I have selected for PATH to be modified only for the current user.
# it installed at C:\Program Files\CMake\

# after installing cmake, python setup.py install command worked... though a few warnings were shown.
#  here are the last two messages during the installation.
# Adding dlib 19.21.0 to easy-install.pth file
# Installed c:\users\guru prasad\appdata\local\programs\python\python39\lib\site-packages\dlib-19.21.0-py3.9-win-amd64.egg


# above process is used to install dlib library on default location.
# how to install on the pycharm environment , we need to install the same using project setting -> interpretter
# install library.

# One way to do it : In PyCharm, Files > Settings > "Project:<nameofyourproject> > Project Interpreter , " \
#                                                   "you can see the current Python interpreter used by PyCharm " \
#                                                   "for your project on the top of the window. Once your environment " \
#                                                   "is properly set, you can install dlib directly from PyCharm

# when i tried that proces, it took a lot of time but installed the dlib.


# Download the pre-trained model here
# http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
# extract the .bz2 file using 7-zip file manager

# https://matthewearl.github.io/2015/07/28/switching-eds-with-python/

import dlib

#path to .dat file
PREDICTOR_PATH = "dlib/shape_predictor_68_face_landmarks.dat"

#1. create predictor object.
predictor = dlib.shape_predictor(PREDICTOR_PATH)

#2. create detector
detector = dlib.get_frontal_face_detector()

# FACE_POINTS = list(range(17, 68))
# MOUTH_POINTS = list(range(48, 61))
# RIGHT_BROW_POINTS = list(range(17, 22))
# LEFT_BROW_POINTS = list(range(22, 27))
# RIGHT_EYE_POINTS = list(range(36, 41))
# LEFT_EYE_POINTS = list(range(42, 48))
# NOSE_POINTS = list(range(27, 35))
# JAW_POINTS = list(range(0, 17))


def get_landmarks(image):
    rects = detector(image,1) # what is this 1 here?
    if len(rects) > 1 :
        pass # do nothing
    if len(rects ) == 0 :
        pass # do nothing.
    # when it contains just one face.
    rect = rects[0]
    print(rect)
    # note the structure of rect object
    # [ (left, top) (right, bottom)] note that there is no common seperating those two points.
    top = rect.top()
    left = rect.left()
    right = rect.right()
    bottom = rect.bottom()

    cv2.rectangle(image,(left,top),(right,bottom),(0,0,255),1)

    parts = predictor(image, rects[0]).parts()
    list = []
    for part in parts:
        list.append([part.x,part.y])
    # list_of_part_coor = np.array(list)
    return list

def mark_landmarks(image, parts_coor):
    print(parts_coor)
    if len(parts_coor) != 0 :
        for (x,y) in parts_coor:
            cv2.circle(image,(x,y),2, (255,0,0),2)


image = cv2.imread("images/shivanshu.jpg")
# image = cv2.imread("images/shivu.jpg")
# image = cv2.imread("images/chetu.jpg")
# image = cv2.imread("images/chetu2.jpg")
# image = cv2.imread("images/face1.jpg")


part_coordinates = get_landmarks(image)
mark_landmarks(image, part_coordinates)

cv2.imshow("Face with landmarks", image)

cv2.waitKey(0)
cv2.destroyAllWindows()



import cv2
import numpy as np
import matplotlib.pyplot as plt


file = "images/stars.jpg"
filetemplate = "images/stars_template.jpg"

# img = cv2.imread(file)
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# img2 = imgGray.copy()
#
# # cv2.imshow("gray", imgGray)
#
# template = cv2.imread(filetemplate)
# templateGray = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
# w, h = templateGray.shape[::-1]
#
# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#             'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
#
# for type in methods:
#     img = img2.copy()
#     method = eval(type)
#
#     # Apply template Matching
#     res = cv2.matchTemplate(img,templateGray,method)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#
#     # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
#     if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#         top_left = min_loc
#     else:
#         top_left = max_loc
#     bottom_right = (top_left[0] + w, top_left[1] + h)
#
#     cv2.rectangle(img,top_left, bottom_right, (0,0,255), 2)
#     print(top_left, bottom_right)
#
#     plt.subplot(121),plt.imshow(res,cmap = 'gray')
#     plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
#     plt.subplot(122),plt.imshow(img,cmap = 'gray')
#     plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
#     plt.suptitle(type)
#
#     plt.show()
#
#


# cv2.matchShapes()
# cv2.matchTemplate()

# ########### Multiple selection ###############
# file = "images/stars.jpg"
# filetemplate = "images/stars_template.jpg"
#
# file = "images/flowers.jpg"
# filetemplate = "images/flower.png"
#
#
# img = cv2.imread(file)
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# img2 = imgGray.copy()
#
# template = cv2.imread(filetemplate)
# templateGray = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
# w, h = templateGray.shape[::-1]
#
# res = cv2.matchTemplate(imgGray,templateGray,cv2.TM_CCOEFF_NORMED)
# print(len(res))
# threshold = 0.90 # change its for accuracy
# loc = np.where( res >= threshold)
# print(len(loc))
# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
#
# cv2.imshow("marked items",img)

########### Multiple selection ###############

########### Match shapes ###############

# Load the shape template or reference image
template = cv2.imread('images/template_shape.jpg', 0)
# cv2.imshow('Template', template)
cv2.waitKey()

# Load the target image with the shapes we're trying to match
target = cv2.imread('images/shapesToMatch.jpg')
target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

# Threshold both images first before using cv2.findContours
ret, thresh1 = cv2.threshold(template, 127, 255, 0)
ret, thresh2 = cv2.threshold(target_gray, 127, 255, 0)

# cv2.imshow("t1",thresh1)
# cv2.imshow("t2",thresh2)


# Find contours in template
contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

print("template",len(contours))
# We need to sort the contours by area so that we can remove the largest
# contour which is the image outline
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

# We extract the second largest contour which will be our template contour
template_contour = contours[1]

# cv2.drawContours(template, [template_contour], -1, (0, 255, 255), 3)
# cv2.imshow('template 1', template)

cv2.drawContours(target, [template_contour], -1, (0, 0, 255), 4)
# cv2.imshow('template 1', template)


# Extract contours from second target image
contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

print("all shapes",len(contours))


for c in contours:
    # Iterate through each contour in the target image and
    # use cv2.matchShapes to compare contour shapes
    match = cv2.matchShapes(template_contour, c, 3, 0.0)
    print(match)
    # If the match value is less than 0.15 we
    if match < .15:
        closest_contour = c
        print("match found")
    else:
        closest_contour = []
    if (len(closest_contour) > 0 ):
        cv2.drawContours(target, [closest_contour], -1, (0, 255, 0), 3)
        cv2.imshow('Output', target)
        # cv2.waitKey(0)
    else:
        print("no match")

k = cv2.waitKey(0)
cv2.destroyAllWindows()


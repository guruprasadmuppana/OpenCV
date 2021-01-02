import cv2
import numpy as np

img = cv2.imread("images/shapes.png")
# img = cv2.imread("images/stars.jpg")
imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("original gray image", imgGray)

imgWithContours = img.copy()

# show the images edges using canny function'

imgCanny = cv2.Canny(imgGray,30,200)
# cv2.imshow("Images with canny edges", imgCanny)

# need to type of contours and type of connections
# cv2.CHAIN_APPROX_SIMPLE provides only minimal points whereas CHAIN_APPROX_NONE collects all points
contours, heirarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# contours, heirarchy = cv2.findContours(imgCanny,cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# cv2.findContours(image, Retrieval Mode, Approximation Method)

cv2.drawContours(img,contours,-1, (0,222,0),2)
# cv2.imshow("image with contours",img)
print(len(contours))
print(len(heirarchy))

# # sort them based on contour areas.
# contourAreas=[]
# for contour in contours:
#     area = cv2.contourArea(contour)
#     contourAreas.append(area)
# print(contourAreas)

# sort them using the areas.
sortedContours = sorted(contours,key=cv2.contourArea, reverse=True)
print(len(sortedContours))


# 1. Draw contours
# draw and show before proceeding to next drawing.
for cnt in sortedContours:
    cv2.drawContours(imgWithContours,[cnt], -1, (255,255,0),3)
    # cv2.imshow("sorted contours on the original image", imgWithContours)
    # cv2.waitKey(0)

# 2. draw centroid of the contours
# Cx=M10/M00 and Cy=M01/M00
def centroid(moments):
    # moments is a dict object
    if (int(moments['m00']) == 0):
        return (0,0)
    cx = int(moments['m10'] / moments['m00'])
    cy = int(moments['m01'] / moments['m00'])
    return (cx,cy)
# find out the centroid of the contours.
for cnt in sortedContours:
    moments= cv2.moments(cnt)
    x,y = centroid(moments)
    cv2.circle(imgWithContours, (x,y), 3,  (255,0,255),3)

# 3. mark left to right with the number
def centroid_x(contours):
    moments = cv2.moments(contours)
    if (int(moments['m00']) == 0):
        return (0)
    cx = int(moments['m10'] / moments['m00']) # it is array of cx
    return cx
contours_L2R = sorted(contours, key=centroid_x, reverse = False)

for k, cnt in enumerate(contours_L2R):
    moments = cv2.moments(cnt)
    x, y = centroid(moments)
    pos=10
    cv2.putText(imgWithContours,str(k+1),(x+pos,y+pos),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),1)

# 4. find bound boxes
for cnt in contours:
    (x,y,w,h) = cv2.boundingRect(cnt)
    cv2.rectangle(imgWithContours,(x,y),(x+w,y+h),(0,0,255),1)

# 5. Draw approximate polygone with percentage of accuracy.
# generally the accuracy is calculated as percentage of perimeter.
# perimeter can be found using arclengh of contours
# best example is circle becomes n-sided polygone

for cnt in contours:
    accuracy = 0.03*cv2.arcLength(cnt,closed=True)
    # find approximate polygone
    approxPolygone = cv2.approxPolyDP(cnt,accuracy,True)
    cv2.drawContours(imgWithContours,[approxPolygone],0,(123,0,255),5)

# 6. convext hull.


# Sort Contors by area and then remove the largest frame contour
n = len(contours) - 1
print("N",n)
sorted(contours, key=cv2.contourArea, reverse=False)
contours = contours[:n] # do not consider first

# Iterate through contours and draw the convex hull
# you would notice for a start object ... it will create convext hull
for cnt in contours:
    hull = cv2.convexHull(cnt)
    cv2.drawContours(imgWithContours, [hull], 0, (0, 255, 0), 2)
    # cv2.imshow('Convex Hull', imgWithContours)
    # cv2.waitKey(0)

cv2.imshow("sorted contours on the original image", imgWithContours)


cv2.waitKey(0)
cv2.destroyAllWindows()
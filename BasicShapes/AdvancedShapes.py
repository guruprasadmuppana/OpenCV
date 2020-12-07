import cv2
import numpy as np


def point(img, pt,color,size=1,thickness=-1):
    cv2.circle(img, pt,size,color, thickness)


def triangle(img, p1,p2,p3,color,thickness):
    cv2.line(img, p1, p2, color, thickness)
    cv2.line(img, p2, p3, color, thickness)
    cv2.line(img, p3, p1, color, thickness)

def square(img,centerPoint, side,color,thickness):

    px,py = centerPoint
    halfSide = int(side / 2.0)

    p1 = (px + halfSide, py - halfSide)
    p2 = (px + halfSide, py + halfSide)
    p3 = (px - halfSide, py + halfSide)
    p4 = (px - halfSide, py - halfSide)

    cv2.line(img, p1, p2, color, thickness)
    cv2.line(img, p2, p3, color, thickness)
    cv2.line(img, p3, p4, color, thickness)
    cv2.line(img, p4, p1, color, thickness)

# defining parameters
size = 500
height,width = (size, size)
channels = 3

blackboard = np.zeros((height, width, channels), np.uint8)


# Triangle
p1 = (400, 100)
p2 = (300, 450)
p3 = (50, 120)

color = (255,0.0)
thickness = 1

triangle(blackboard, p1,p2,p3,color,thickness)
cv2.imshow("blackboard",blackboard)

# Square
centerPoint = (250,250)
side = 200
square(blackboard,centerPoint,side,color,thickness )
cv2.imshow("blackboard",blackboard)


# Ploting points.
point(blackboard,centerPoint,color)
point(blackboard, p1, color,size=3)
point(blackboard, p2, color,size=10)

cv2.imshow("blackboard", blackboard)

#Polygon:
#cv2.polylines(image, [pts], isClosed, color, thickness)
pts1 = np.array([[300,200],[350,225],[400,300],[250,350],[350,100]], np.int32)
# pts = pts.reshape((-1, 1, 2))
imgGraph =cv2.polylines(blackboard, [pts1], True, color, thickness=2)

# fillConvextPoly
pts2 = np.array([[50, 300], [100, 300], [75, 400]])
# pts2 = np.array([[50, 300], [100, 300], [75, 400],[350,100]])
cv2.fillConvexPoly(blackboard, pts2, color)

#fillPoly
pts3 = np.array([[50, 50],  [50, 75],[100, 100]])
pts4 = np.array([[100, 50],  [150, 75],[200, 50],[250, 10]])
color = (0,255,00)
cv2.fillPoly(blackboard,[pts3,pts4],color)

cv2.imshow("blackboard",blackboard)

cv2.waitKey(0)
cv2.destroyAllWindows()
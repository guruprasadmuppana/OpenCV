import cv2
import numpy as np


def pointFunction(img, pt,color,size=1,thickness=-1):
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

# triangle(blackboard, p1,p2,p3,color,thickness)
# cv2.imshow("blackboard",blackboard)
#
# Square
# centerPoint = (250,250)
# side = 200
# square(blackboard,centerPoint,side,color,thickness )
# cv2.imshow("blackboard",blackboard)
#
# # Ploting points.
# point(blackboard,centerPoint,color)
# point(blackboard, p1, color,size=3)
# point(blackboard, p2, color,size=10)
#
# cv2.imshow("blackboard", blackboard)

# Polygon:
# #cv2.polylines(image, [pts], isClosed, color, thickness)
# pts1 = np.array([[300,200],[350,225],[400,300],[250,350],[350,100]], np.int32)
# cv2.polylines(blackboard, [pts1], True, color, thickness=3)

# # fillConvextPoly
# pts2 = np.array([[50, 300], [100, 300], [75, 400]])
# # pts2 = np.array([[50, 300], [100, 300], [75, 400],[350,100]])
# cv2.fillConvexPoly(blackboard, pts2, color)

# #fillPoly
# pts3 = np.array([[50, 50],  [50, 75],[100, 100]])
# pts4 = np.array([[100, 50],  [150, 75],[200, 50],[250, 10]])
# color = (0,255,00)
# cv2.fillPoly(blackboard,[pts3,pts4],color)

cv2.imshow("blackboard",blackboard)


# # interactive polygones
# points = []
# flagPolygon = False
#
# #setup a callback
# def mouseClick(event,x,y,flags, params):
#     # print("Mouse is clicked")
#     global flagPolygon
#     if (event == cv2.EVENT_LBUTTONDOWN):
#         if (flagPolygon):
#             points.clear()
#         flagPolygon = False
#         # capture the x, y point
#         print(x, y)
#         points.append([x,y])
#     elif (event == cv2.EVENT_RBUTTONDOWN):
#         print("Right click")
#         flagPolygon = True
#
# cv2.namedWindow("blackboard")
# cv2.setMouseCallback("blackboard", mouseClick)
#
# while True:
#     if len(points) == 0:
#         pass
#     elif len(points) == 1 :
#         point = points[-1]
#         pt = (x,y) = point[0],point[1]
#         pointFunction(blackboard,pt,color,size=5)
#     elif len(points) == 2 :
#         linep1 = points[0]
#         linep2 = points[1]
#         lineP1_xy = (x,y) = linep1[0],point[1]
#         lineP2_xy = (x,y) = linep2[0], linep2[1]
#         cv2.line(blackboard,lineP1_xy,lineP2_xy,color,thickness=1)
#     elif len(points) > 2:
#         ptsArray = np.array(points)
#         cv2.polylines(blackboard, [ptsArray], flagPolygon, color, thickness=2)
#
#     cv2.imshow("blackboard",blackboard)
#     k =cv2.waitKey(1)
#     if k == 27:
#         break


cv2.waitKey(0)
cv2.destroyAllWindows()
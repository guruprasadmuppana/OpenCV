import cv2
import numpy as np

size = 500
height,width = (size, size)


graphFile = "images/graph.png"
imgGraph = cv2.imread(graphFile)
cv2.imshow("Graph",imgGraph)

channels = 3
color = (255, 0, 255)  # Pink color
thickness = 2


# Drawing line
start_point = (50,50)
end_point = (50,100)
imgGraph = cv2.line(imgGraph, start_point, end_point, color, thickness)
cv2.imshow("Graph",imgGraph)



# ArrowedLine
shift=20
start_point = (50+shift,50)
end_point = (50+shift,100)
tipLength = 0.3 # defect value
imgGraph = cv2.arrowedLine(imgGraph, start_point, end_point,color, thickness, tipLength=tipLength )
cv2.imshow("Graph",imgGraph)

#
#Double arrow line
# ArrowedLine
shift=40
start_point = (50+shift,50)
end_point = (50+shift,100)
tipLength = 0.3 # defect value
imgGraph = cv2.arrowedLine(imgGraph, start_point, end_point,color, thickness, tipLength=tipLength )
imgGraph = cv2.arrowedLine(imgGraph, end_point, start_point,color, thickness, tipLength=tipLength )
cv2.imshow("Graph",imgGraph)


#Rectangle
start_point = (25,200)
end_point = (100,250)
imgGraph = cv2.rectangle(imgGraph, start_point, end_point, color, thickness)
cv2.imshow("Graph",imgGraph)


#Circle
#center and radius
centerX,centerY = 150,150
radius = 50
imgGraph = cv2.circle(imgGraph, (centerX, centerY), radius,  color, thickness)
cv2.imshow("Graph",imgGraph)



# Ellipse
#center and radius
center = (centerX,centerY) = (300,150)
axes = (axesX, axesY) = (50,25)
angle = 30  # angle which the axes rotated. 30
startAngle = 00
endAngle = 360 # 270
thickness = -1 # for filling

imgGraph = cv2.ellipse(imgGraph, (centerX,centerY), (axesX,axesY),
                    angle, startAngle, endAngle, color, thickness)
cv2.imshow("Graph",imgGraph)



#########


#Trackbar Setup
cv2.namedWindow('Trackbars')
def callback(x):
    pass
# create trackbars for color change
cv2.createTrackbar('R','Trackbars',100,255,callback)
cv2.createTrackbar('G','Trackbars',10,255,callback)
cv2.createTrackbar('B','Trackbars',0,255,callback)
cv2.createTrackbar('Radius','Trackbars',50,100,callback)


while(True):

    # get current positions of the trackbars
    r = cv2.getTrackbarPos('R','Trackbars')
    g = cv2.getTrackbarPos('G','Trackbars')
    b = cv2.getTrackbarPos('B','Trackbars')
    circle_radius = cv2.getTrackbarPos('Radius','Trackbars')

    dynamic_color = (b,g,r)

    # Text
    font = cv2.FONT_HERSHEY_SIMPLEX
    origin = (150, 50)  # bottom-left
    fontScale = 1  # Multiple of basic size of the font. It can be more than 1 and even less than 1
    thickness = 2
    image = cv2.putText(imgGraph, "Basic Shapes", origin, font, fontScale, dynamic_color, thickness, cv2.LINE_AA)

    imgGraph = cv2.circle(imgGraph, (200, 300), circle_radius, dynamic_color, thickness)

    cv2.imshow('Graph',imgGraph)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # esc key
        break



cv2.waitKey(0)
cv2.destroyAllWindows()

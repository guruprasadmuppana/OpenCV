import cv2
import numpy as np

size = 500
height,width = (size, size)
channels = 3
# create an image with two dimenstion array. Color channel are not consider here.
blackboard = np.ndarray([height,width,channels])
# Initailizing all pixels black (zero)
blackboard[:,:,:]= 0

# blackboard = np.zeros((height, width, 3), np.uint8)

# Display the blackboard
# cv2.imshow("blackboard",blackboard)

graphFile = "images/graph.png"
imgGraph = cv2.imread(graphFile)
# cv2.imshow("graph",imgGraph)

# Drawing line
start_point = (50,50)
end_point = (50,150)
color = (255,0,255) # Pink color
thickness = 2
# imgGraph = cv2.line(imgGraph, start_point, end_point, color, thickness)
background = cv2.line(blackboard, start_point, end_point, color, thickness)

imgGraph = cv2.line(imgGraph, start_point, end_point, color, thickness,lineType=-1, shift=0)

# cv2.imshow("Line",imgGraph)
# cv2.imshow("blackboard",blackboard)

# ArrowedLine
shift=20
start_point = (50+shift,50+shift)
end_point = (50+shift,450+shift)
tipLength = 0.1 # defect value
imgGraph = cv2.arrowedLine(imgGraph, start_point, end_point,color, thickness,line_type=4, shift=1)
background = cv2.arrowedLine(background, start_point, end_point,color, thickness, tipLength=0.05 )

# cv2.imshow("Line",imgGraph)
# cv2.imshow("blackboard",blackboard)


#Rectangle
start_point = (100,100)
end_point = (200,200)
imgGraph = cv2.rectangle(imgGraph, start_point, end_point, color, thickness)
background = cv2.rectangle(background, start_point, end_point, color, thickness)

# cv2.imshow("Line",imgGraph)
# cv2.imshow("blackboard",blackboard)

#Circle
#center and radius
centerX,centerY = 400,200
radius = 100
imgGraph = cv2.circle(imgGraph, (centerX, centerY), radius,  color, thickness)
background = cv2.circle(blackboard, (centerX, centerY),radius, color, thickness)

# cv2.imshow("Line",imgGraph)
# cv2.imshow("blackboard",blackboard)

# Ellipse
#center and radius
center = (centerX,centerY) = (200,400)
axes = (axesX, axesY) = (75,50)
angle = 30  # angle which the axes rotated.
startAngle = 0
endAngle = 360
thickness = -1


imgGraph = cv2.ellipse(imgGraph, (centerX,centerY), (axesX,axesY),
                    angle, startAngle, endAngle, color, -1)
blackboard = cv2.ellipse(blackboard, center, axes,
                    angle, startAngle, endAngle, color, thickness)


cv2.imshow("Graph",imgGraph)
cv2.imshow("black board",blackboard)

# Text
font = cv2.FONT_HERSHEY_SIMPLEX
origin = (50, 50) # bottom-left
fontScale = 1 # Multoiple of basic size of the font. It can be more than 1 and even less than 1
thickness = 2

image = cv2.putText(imgGraph, "Basic Shapes", origin, font,fontScale, color, thickness,cv2.LINE_AA)
image = cv2.putText(blackboard, "Basic Shapes", origin, font,fontScale, color, thickness,cv2.LINE_AA)

cv2.imshow("Graph",imgGraph)
cv2.imshow("black board",blackboard)


cv2.waitKey(0)
cv2.destroyAllWindows()

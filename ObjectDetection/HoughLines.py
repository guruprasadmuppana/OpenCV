
import cv2
import numpy as np

image = cv2.imread('images/window1.jpg')
# image = cv2.imread('images/road1.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray, 100, 170, apertureSize = 3)

# grayBlur = cv2.GaussianBlur(gray, (5, 5), 10)
grayBlur = cv2.medianBlur(gray, 7)
edges = cv2.Canny(grayBlur, 50, 200 )
# edges = cv2.Canny(gray, 180, 255 )
cv2.imshow("canny",edges)

# lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, 10, 10) # max_slider = 200
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 30)

# print(lines.shape)
print(len(lines))
for line in lines:
    # for x1, y1, x2, y2 in lines[0]:
    x1, y1, x2, y2 = line[0]
    cv2.line(image, (x1, y1), (x2, y2),(0, 255, 0), 3)
    # cv2.waitKey(0)

cv2.imshow('Probabilistic Hough Lines', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
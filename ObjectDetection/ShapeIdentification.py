import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# not a good method to detect the shapes.

file = "images/shapes.png"
# # file = "images/temple.jpg"
# file = "images/window1.jpg"
img = cv.imread(file)
img_gray = cv.imread(file,cv.IMREAD_GRAYSCALE)
# cv2.imshow("shapes original",imggray)

_, thresh = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)

contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


# contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

for c in contours:
    approx = cv.approxPolyDP(c, 0.05 * cv.arcLength(c, True), True) # try one 1 and 5 percetage
    cv.drawContours(img, [approx], 0, (0, 255, 0), 1)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    if len(approx) == 3:
        cv.putText(img, "Triangle", (x, y),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
    elif len(approx) == 4:
        x1, y1, w, h = cv.boundingRect(approx)

        cv.rectangle(img, (x1,y1),(x1+w,y1+h),(255,0,0),3)
        aspect_ratio = float(w) / float(h)
        print(aspect_ratio)
        if aspect_ratio >= 0.95 and aspect_ratio <= 1.05:
            cv.putText(img, "Square", (x, y),
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
        else:
            cv.putText(img, "Rectangle", (x, y),
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
    elif len(approx) == 5:
        cv.putText(img, "Pentagon", (x, y),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
    elif len(approx) == 10:
        cv.putText(img, "Star", (x, y),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
    else:
        cv.putText(img, "Circle", (x, y),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)

cv.imshow("Shapes", img)
cv.waitKey()
cv.destroyAllWindows()

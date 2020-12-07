
import cv2
import numpy as np
import matplotlib.pyplot as plt


file = "Images/hair1.jpg"

# Reading the image
img = cv2.imread(file)

# converted into RGB colors
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#Convert two D image into 3 D
imgGray= cv2.cvtColor(imgGray, cv2.COLOR_GRAY2RGB)


# Negative Image
imgInv= cv2.bitwise_not(img)

# Flips image
imgflip= cv2.flip(img,0) # 0 for vertical flip and 1 for horizontal flip


plt.subplot(141)
plt.imshow(img)
plt.title("Original")

plt.subplot(142)
plt.imshow(imgGray)
plt.title("gray")

plt.subplot(143)
plt.imshow(imgInv)
plt.title("invert")
#
plt.subplot(144)
plt.imshow(imgflip)
plt.title("Flip")


plt.show()



# Wait until any key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()



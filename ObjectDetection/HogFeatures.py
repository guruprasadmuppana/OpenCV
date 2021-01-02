import cv2
import numpy as np
import matplotlib.pyplot as plt


# in this program, we will cover the HOG features.
# HOG stands for Histogram of Gradients

# steps: First selecte cell, block and orientations size.
cell_size = (8,8)
block_size = (2,2) # block contains the cells
orientations = 9
# read the image and find out its size:
img = cv2.imread("images/flowers.jpg")
# img = cv2.imread("images/stars.jpg")
# img = cv2.imread("images/sudoku.png")



imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgGrayBlur = cv2.GaussianBlur(imgGray, (3,3),0)
imgCanny = cv2.Canny(imgGrayBlur, 100, 180)
# cv2.imshow("Canny image",imgCanny)

img = imgCanny.copy()

# image shape
w,h = img.shape[:2] # first two parameters of shape tuple
# print(w,h)
print(img.shape)
# print(type(img.shape))
winSize = (h // cell_size[1])*cell_size[1], (w //cell_size[0])*cell_size[0]
print(winSize)
block_size_p = block_size[1]*cell_size[1], block_size[0]*cell_size[0]
block_stride = cell_size[1], cell_size[0] # can we not directly assign cell_size.
# it is found that in the image, height (rows) vs width (columns)

# let us call now the HOG feature. first step is to iniitiate with various parameters
hog = cv2.HOGDescriptor(_winSize=winSize,
                        _blockSize=block_size_p,
                        _blockStride=block_stride,
                        _cellSize=(cell_size[1],cell_size[0]),
                        _nbins=orientations)

# Create numpy arrage size from the image.
n_cell_shape = img.shape[0] // cell_size[0], img.shape[1] // cell_size[1]

print(n_cell_shape)

hog_features_array = hog.compute(imgGray)
# hog_features_array = hog.compute(imgCanny)


hog_features_reshape = hog_features_array.reshape(n_cell_shape[1]-block_size[1]+1,
                                          n_cell_shape[0]-block_size[0]+1,
                                          block_size[0],block_size[1],
                                          orientations)
print(hog_features_reshape.shape)
hog_features = hog_features_reshape.transpose(1,0,2,3,4)

print(hog_features.shape)

gradients = np.zeros((n_cell_shape[0],n_cell_shape[1],orientations))
cell_count= np.full((n_cell_shape[0],n_cell_shape[1],1),
                    0,
                    dtype=int)

# block normalization.
for off_y  in range(block_size[0]):
    for off_x in range(block_size[1]):
        gradients[off_y:n_cell_shape[0] - block_size[0]+ off_y + 1,
                  off_x:n_cell_shape[1] - block_size[1]+ off_x + 1] += hog_features[:,:,off_y,off_x,:]
        cell_count[off_y:n_cell_shape[0] - block_size[0]+ off_y + 1,
                  off_x:n_cell_shape[1] - block_size[1]+ off_x + 1] += 1


# average gradients
gradients /= cell_count

# print(cell_count)

color_bins = 5
plt.pcolor(gradients[:,:,color_bins])
plt.gca().invert_yaxis()
plt.gca().set_aspect('equal',adjustable='box')
plt.colorbar()
plt.show()

print(gradients.shape)
# cv2.imshow("gradients",gradients)

cv2.waitKey(0)
cv2.destroyAllWindows()


###########
# https://stackoverflow.com/questions/6090399/get-hog-image-features-from-opencv-python
# 1. Get Inbuilt Documentation: Following command on your python console will help you know the structure of class HOGDescriptor:
#
#  import cv2;
#  help(cv2.HOGDescriptor())
# 2. Example Code: Here is a snippet of code to initialize an cv2.HOGDescriptor with different parameters (The terms I used here are standard terms which are well defined in OpenCV documentation here):
#
# import cv2
# image = cv2.imread("test.jpg",0)
# winSize = (64,64)
# blockSize = (16,16)
# blockStride = (8,8)
# cellSize = (8,8)
# nbins = 9
# derivAperture = 1
# winSigma = 4.
# histogramNormType = 0
# L2HysThreshold = 2.0000000000000001e-01
# gammaCorrection = 0
# nlevels = 64
# hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins,derivAperture,winSigma,
#                         histogramNormType,L2HysThreshold,gammaCorrection,nlevels)
# #compute(img[, winStride[, padding[, locations]]]) -> descriptors
# winStride = (8,8)
# padding = (8,8)
# locations = ((10,20),)
# hist = hog.compute(image,winStride,padding,locations)
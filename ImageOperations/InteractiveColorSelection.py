import cv2
import numpy as np

colorsfile = "images\colorBlocks.jpg"
# # colorsfile = "images\Diamond-Jewelry.jpg"
colorsfile = "images/bangles1.jpg"
# # colorsfile = "images\saree2.jpg"
# colorsfile = "images\saree3.jpg"
# # colorsfile = "images\saree4.jpg"

imgColors = cv2.imread(colorsfile)
cv2.imshow("Color Blocks",imgColors)

imgColors_HSV = cv2.cvtColor(imgColors,cv2.COLOR_BGR2HSV)

# bluemin = np.array([100, 60, 60], np.uint8)
# bluemax = np.array([140, 255, 255], np.uint8)
# blue_block_mask = cv2.inRange(imgColors_HSV,bluemin,bluemax)
# blue_areas = cv2.bitwise_and(imgColors,imgColors,mask=blue_block_mask )
# cv2.imshow("Blue Areas",blue_areas)


# red1min = np.array([0, 100, 100], np.uint8)
# red1max = np.array([10, 255, 255], np.uint8)
# red2min = np.array([160, 100, 100], np.uint8)
# red2min = np.array([179, 255, 255], np.uint8)
# red1_block_mask = cv2.inRange(imgColors_HSV,red1min,red1max)
# red2_block_mask = cv2.inRange(imgColors_HSV,red2min,red2min)
# red_block_mask = cv2.bitwise_or(red1_block_mask,red2_block_mask)
# red_areas = cv2.bitwise_and(imgColors,imgColors,mask=red_block_mask )
# cv2.imshow("Red Areas",red_areas)
#
# greenmin = np.array([50, 52, 72], np.uint8) # 60,60 for S and L will work;52, 72
# greenmax = np.array([70, 255, 255], np.uint8)
# green_block_mask = cv2.inRange(imgColors_HSV,greenmin,greenmax)
# green_areas = cv2.bitwise_and(imgColors,imgColors,mask=green_block_mask )
# cv2.imshow("Green Areas",green_areas)


# conversion BGR to HSV
color = np.uint8([[[255,0,0 ]]])
hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
print( "Color",hsv_color )

def mouse_click(event,x,y, flag, param):
    if (event == cv2.cv2.EVENT_LBUTTONDOWN):
        print ("XY",x,y)
        selectColor = imgColors[y,x]
        color = np.uint8([[[selectColor[0],selectColor[1],selectColor[2] ]]])
        hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
        hue = hsv_color[0][0][0]
        sat = hsv_color[0][0][1]
        val = hsv_color[0][0][2]

        print ("HSV Color:",hsv_color[0][0][0])
        # low [H-10, 100,100] ;  high [H+10, 255, 255]
        band = 10
        colormin = np.array([hue-band, 100, 100])  # S,v= 100,100
        colormax = np.array([hue+band, 255, 255]) # s,v = 255.255
        color_block_mask = cv2.inRange(imgColors_HSV, colormin, colormax)
        color_block_mask_inv = cv2.bitwise_not(color_block_mask)
        color_areas = cv2.bitwise_and(imgColors, imgColors, mask=color_block_mask)
        cv2.imshow("color areas", color_areas)

cv2.setMouseCallback('Color Blocks', mouse_click)


cv2.waitKey(0)
cv2.destroyAllWindows()





############

# colorsfile = "images/black_ground_images.jpg"
# colorsfile = "images/blue_focus_flower.jpg"


# #white
# whitemin = np.array([0, 35, 0]) # 42
# whitemax = np.array([179, 255, 255])
# white_block_mask = cv2.inRange(imgColors_HSV,whitemin,whitemax)
# white_block_mask_inv = cv2.bitwise_not(white_block_mask)
# white_areas = cv2.bitwise_and(imgColors,imgColors,mask=white_block_mask_inv )
# cv2.imshow("white Areas",white_areas)

# #black
# blackmin = np.array([0, 0, 0])
# blackmax = np.array([179, 255, 60])
# black_block_mask = cv2.inRange(imgColors_HSV,blackmin,blackmax)
# # cv2.imshow("mask",black_block_mask)
# black_block_mask_inv = cv2.bitwise_not(black_block_mask)
# # cv2.imshow("mask inv",black_block_mask_inv)
# black_areas = cv2.bitwise_and(imgColors,imgColors,mask=black_block_mask )
# cv2.imshow("Black Areas",black_areas)

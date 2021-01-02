import cv2

image1 = cv2.imread("Images/temple.jpg")
# cv2.imshow("image1", image1);
logo = cv2.imread("Images/sunflower_small.jpg")
# cv2.imshow("image2", logo);

#
rows,cols,channels = logo.shape
logoArea = image1[0:rows, 0:cols ] # Crop the image with the logo size

# # Paste operation
# image3=image1.copy()
# image3[0:rows, 0:cols ] = logo
# cv2.imshow("Paste",image3)

img2gray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray",img2gray)
ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)
# cv2.imshow("mask",mask)
mask_inv = cv2.bitwise_not(mask)
# cv2.imshow("mask inv",mask_inv)


forground_with_mask = cv2.bitwise_and(logo,logo,mask = mask)
# cv2.imshow("foreground",forground_with_mask)

backgrond_with_mask = cv2.bitwise_and(logoArea,logoArea,mask=mask_inv)
# cv2.imshow("background",backgrond_with_mask)

# final_img = cv2.add(forground_with_mask,backgrond_with_mask)
# image1[0:rows, 0:cols ] = final_img
# cv2.imshow("final",image1)


# final_img = cv2.add(image1,image2)
# cv2.imshow("Pixel addition",final_img)


video = cv2.VideoCapture("images/171124_B1_HD_001.mp4") # 0 for Defautl Video or WebCam

while (True):
    _,frame = video.read()
    # rows, cols, channels = logo.shape
    logoArea = frame[0:rows, 0:cols]  # Crop the image with the logo size
    # img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
    # ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)
    # mask_inv = cv2.bitwise_not(mask)
    # forground_with_mask = cv2.bitwise_and(logo, logo, mask=mask)
    backgrond_with_mask = cv2.bitwise_and(logoArea, logoArea, mask=mask_inv)
    final_img = cv2.add(forground_with_mask, backgrond_with_mask)
    frame[0:rows, 0:cols] = final_img

    cv2.imshow("Default Video",frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break




cv2.waitKey(0)
cv2.destroyAllWindows()


#
# for i in range(100):
#     percentage = float(i/100)
#     print(percentage)
#     imgAdd = cv2.addWeighted(image2,percentage,image1,1-percentage,0)
#     cv2.imshow("Morphed", imgAdd);

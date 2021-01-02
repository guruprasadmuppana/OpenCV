import cv2

image1 = cv2.imread("Images/parrot.jpg") # rahul
# cv2.imshow("image1", image1)
image2 = cv2.imread("Images/macaw.jpg") # modi
# cv2.imshow("image2", image2)

# imgAdd = cv2.addWeighted(image1,0.7,image2,0.3,0) # the last 0 is gamma.. it will be added to all pixel.
# cv2.imshow("Morphed", imgAdd);

slides = [["Images/parrot.jpg","Images/macaw.jpg"],
          ["Images/rahul.jpg","Images/modi.jpg"]]

for src, dst in slides:
    imagesrc = cv2.imread(src)
    imagesrc = cv2.resize(imagesrc,(225,225))
    imagedst = cv2.imread(dst)
    imagedst = cv2.resize(imagedst, (225, 225))

    for i in range(100):
        percentage = float(i/100)
        print(percentage)
        imgAdd = cv2.addWeighted(imagesrc,1-percentage,imagedst,percentage,0)
        cv2.imshow("Morphed", imgAdd);
        cv2.waitKey(100) # waiting 100 milli seconds

cv2.waitKey(0)
cv2.destroyAllWindows()



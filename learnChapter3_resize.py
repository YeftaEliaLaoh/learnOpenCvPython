import cv2

print("package imported")

img = cv2.imread("Resources/lambo.jpg")
print(img.shape)

imgResize = cv2.resize(img,(720,320))
print(imgResize.shape)

imgCropped = imgResize[0:200,200:500]

#cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)
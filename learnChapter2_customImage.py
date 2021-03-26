import cv2
import numpy as np

print("package imported")

kernel = np.ones((5,5),np.uint8)

img = cv2.imread("Resources/Lenna.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgGray,100,100)
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDilation,kernel,iterations=1)

cv2.imshow("Gray",imgGray)
cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Dilate",imgDilation)
cv2.imshow("Erode",imgEroded)

cv2.waitKey(0)
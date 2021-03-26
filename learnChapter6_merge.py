import cv2
import numpy as np


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    imageBlank = np.zeros((height, width, 3), np.uint8)

    for x in range(0, rows):
        for y in range(0, cols):
            if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
            else:
                imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None,
                                            scale, scale)
            if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)

    hor = [imageBlank]*rows
    for x in range(0, rows):
        hor[x] = np.hstack(imgArray[x])
    return np.vstack(hor)

img = cv2.imread('Resources/Lenna.png')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

imgStack = stackImages(0.5,([img,imgGray,img],[img,img,img]))

# imgHor = np.hstack((img,img))
# imgVer = np.vstack((img,img))
#
# cv2.imshow("Horizontal",imgHor)
# cv2.imshow("Vertical",imgVer)
cv2.imshow("ImageStack",imgStack)

cv2.waitKey(0)
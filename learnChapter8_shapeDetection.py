import cv2
import numpy as np


def stackImages(scale, imgArray):
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

    hor = [imageBlank] * rows
    for x in range(0, rows):
        hor[x] = np.hstack(imgArray[x])
    return np.vstack(hor)


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 400:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            aspRatio = w / float(h)

            if objCor ==3: objectType ="Triangle"
            elif objCor == 4:
                if aspRatio >0.98 and aspRatio <1.03: objectType= "Square"
                else:objectType="Rectangle"
            elif objCor== 5: objectType= "Pentagonal"
            elif objCor>5:
                if aspRatio >0.98 and aspRatio <1.03: objectType= "Circle"
                else:objectType="Oval"
            else:objectType="None"

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,objectType,
                        (x,y+(h//2)),cv2.FONT_HERSHEY_COMPLEX,0.7,
                        (0,0,0),2)

path = 'Resources/shapes.png'
img = cv2.imread(path)
imgResize = cv2.resize(img, (480, 320))
imgContour = imgResize.copy()

imgGray = cv2.cvtColor(imgContour, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)

imgBlank = np.zeros_like(imgResize)
imgStack = stackImages(0.8, ([imgResize, imgGray, imgBlur],
                             [imgCanny, imgContour, imgBlank]))

cv2.imshow("Stack", imgStack)
cv2.waitKey(0)

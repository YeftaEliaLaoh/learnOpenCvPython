import cv2
import numpy as np

def empty(a):
    pass

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

path = 'Resources/lambo.jpg'
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",30,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",40,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",158,255,empty)
cv2.createTrackbar("Val Min","TrackBars",36,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

while True:
    img = cv2.imread(path)
    imgResize = cv2.resize(img, (720, 320))

    imgHSV = cv2.cvtColor(imgResize,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(imgResize,imgResize,mask=mask)


    # cv2.imshow("Original",img)
    # cv2.imshow("HSV",imgHSV)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("Result", imgResult)

    imgStack = stackImages(0.6,([imgResize,imgHSV],[mask,imgResult]))
    cv2.imshow("Stacked Images", imgStack)

    cv2.waitKey(1)
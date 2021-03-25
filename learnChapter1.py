import cv2

print("package imported")

# img = cv2.imread("Resources/Lenna.png")
# cv2.imshow("output",img)
# cv2.waitKey(0)

# cap = cv2.VideoCapture("Resources/test_video.mp4")
cap = cv2.VideoCapture(0) #default laptop = 0
cap.set(3,640) # 3 = width
cap.set(4,480) # 4 = height
cap.set(10,50) # 10 = brightness

while True:
    success, img = cap.read()
    cv2.imshow("output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

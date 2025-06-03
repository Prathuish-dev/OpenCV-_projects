import cv2
import numpy as np

img = cv2.imread("assets/shapes.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#SHI-TOMASI METHOD
corners=cv2.goodFeaturesToTrack(gray_img, maxCorners=50,
                                qualityLevel=0.2, minDistance=50)

corners = np.intp(corners)
for c in corners:
    x, y =c.ravel()
    img=cv2.circle(img, center=(x,y),radius=20, color=(0,0,255),thickness=-1)

# HARRIS CORNER DETECTION
corners=cv2.goodFeaturesToTrack(gray_img, maxCorners=50,
                                qualityLevel=0.02, minDistance=50,
                                useHarrisDetector=True, k=0.1)
corners = np.intp(corners)
for c in corners:
    x, y =c.ravel()
    img=cv2.circle(img, center=(x,y),radius=10, color=(0,255,0),thickness=-1)


cv2.imshow("Shapes",img)
cv2.waitKey(0)
cv2.destroyAllWindows

cv2.imwrite("assets/5_shape_w_corners.png",img)

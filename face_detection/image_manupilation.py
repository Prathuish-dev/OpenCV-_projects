import cv2
import numpy as np

img = cv2.imread("assets/mclaren_f1.jpg",  cv2.IMREAD_COLOR)

# RESIZE

img = cv2.resize(img, (800,800))
img=cv2.resize(img, (0,0), fx=2, fy=0.5)


#CROP

height, width = img.shape[0],img.shape[1]
img= img[int(height/3) : height, 50 : -50]


#ROTATE

heifht,width =img.shape[0],img.shape[1]
img=cv2.rotate(img, cv2.ROTATE_180)
M= cv2.getRotationMatrix2D(center=(width/2, height/2),angle=150, scale=1)
img=cv2.warpAffine(img, M,(width, height))


#TRANSLATE

tx= width/ 5
ty= -height/5
#transilation matrix
M=np.array([
    [1, 0, tx],
    [0,1,ty]
])
img=cv2.warpAffine(img, M ,(width, height))

cv2.imshow("F1!", img)
cv2.waitKey(0)
cv2.destroyAllWindows

cv2.imwrite("assets/2_man_f1.jpg", img)
import cv2

img = cv2.imread("assets/mclaren_f1.jpg", cv2.IMREAD_COLOR)
#print(img.size)
print(img.shape)
print(img[0,0])

#img = img * 2
#print(img[0,0])

#for i in range(img.shape[0]):
#    for j in range(img.shape[1]):
#        img[i,j] = max(254, img[i,j]*2)

cv2.imshow("f1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray_img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("assets/grey_f1.jpg", gray_img)
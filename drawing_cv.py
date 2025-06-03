import cv2

img=cv2.imread("assets/mclaren_f1.jpg",cv2.IMREAD_COLOR)

#BORDER
img = cv2.copyMakeBorder(img, 50,50,50,50,
                         borderType=cv2.BORDER_CONSTANT,
                         value=(100,0,0)) #BORDER_CONSTANT  BORDER_REFLECT BORDER_WRAP

#LINE
img = cv2.line(img, (50,50),(500,500), color=(0,200,0),
               thickness=20)

#ARROW
img= cv2.arrowedLine(img,(50,50),(450,300),color=(0,0,200),thickness=10)

#CIRCLE
img=cv2.circle(img, center=(1000,800),radius=50,color=(0,100,200),thickness=-10)

#ELLIPSE
img=cv2.ellipse(img,center=(1000,450),axes=(100,200),
                angle=45, startAngle=0,endAngle=270,color=(100,200,200),
                thickness=30)

#RECTANGLE
img=cv2.rectangle(img,pt1=(250,250),pt2=(1000,850),color=(10,50,124),thickness=30)

#TEXT
img=cv2.putText(img,"mclaren f1 car",org=(300,750),fontFace=cv2.FONT_ITALIC,fontScale=5,
                color=(0,0,0),thickness=10) 

cv2.imshow("f1!",img)
cv2.waitKey(0)
cv2.destroyAllWindows
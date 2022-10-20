import cv2
import numpy as np

img1=cv2.imread('C:/Users/Lenovo/Desktop/test/A3/001.3.png')
img2=cv2.imread('C:/Users/Lenovo/Desktop/test/A3/A3.3.png',0)

ret,img=cv2.threshold(img2,0,255,cv2.THRESH_OTSU|cv2.THRESH_BINARY_INV)
cv2.imwrite('C:/Users/Lenovo/Desktop/test/A3/ddd.png',img)
contours, hierarchy = cv2.findContours(img, cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)

drawing=np.zeros(shape=(img1.shape),dtype=np.uint8)
#print(hierarchy)#[[[-1 -1  1 -1],[-1 -1 -1  0]]]
hierarchy=np.squeeze(hierarchy)#从数组的形状中删除单维条目，即把shape中为1的维度去掉
#print(hierarchy)#[[-1 -1  1 -1],[-1 -1 -1  0]]
for i in range(len(contours)):
    if(hierarchy[i][3]!=-1):#存在父轮廓，说明是里层
        cv2.drawContours(drawing,contours,i,(255,255,255),-1)#填充

cv2.imwrite('C:/Users/Lenovo/Desktop/test/A3/drawing.png',drawing)

result=cv2.bitwise_and(drawing,img1)

cv2.imwrite('C:/Users/Lenovo/Desktop/test/A3/A3.4.png',result)



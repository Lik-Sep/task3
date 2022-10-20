import cv2
import numpy as np

img=cv2.imread('C:/Users/Lenovo/Desktop/test/A3/001.3-bin.png',0)

#膨胀
kernel1=cv2.getStructuringElement(shape=cv2.MORPH_RECT,ksize=(3,3))
dilateimg=cv2.dilate(img,kernel1,iterations=1)
cv2.imwrite('C:/Users/Lenovo/Desktop/test/A3/dilateimg.png',dilateimg)
#腐蚀
kernel=cv2.getStructuringElement(shape=cv2.MORPH_RECT,ksize=(15,15))
erodeimg=cv2.erode(dilateimg,kernel=kernel,iterations=9)
cv2.imwrite('C:/Users/Lenovo/Desktop/test/A3/erodeing.png',erodeimg)
#转换为黑底白字
ret,img1=cv2.threshold(erodeimg,0,255,cv2.THRESH_OTSU|cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

drawing=np.zeros(shape=(img.shape),dtype=np.uint8)+255
#cv2.drawContours(img,contours,-1,(0,0,0), 5, cv2.LINE_8, hierarchy)
#cv2.imwrite('C:/Users/Lenovo/Desktop/test/A3/drawing.png',img)

cv2.drawContours(drawing,contours,-1,(0,0,0), 5, cv2.LINE_8, hierarchy)
cv2.imwrite('C:/Users/Lenovo/Desktop/test/A3/A3.3.png',drawing)
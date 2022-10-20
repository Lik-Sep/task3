import cv2


img=cv2.imread('C:/Users/Lenovo/Desktop/test/A3/001.3-bin.png',0)
kernel=cv2.getStructuringElement(shape=cv2.MORPH_RECT,ksize=(9,9))
erodeimg=cv2.erode(img,kernel=kernel,iterations=1)
cv2.imwrite('C:/Users/Lenovo/Desktop/test/A3/3.2.1.png',erodeimg)

kernel1=cv2.getStructuringElement(shape=cv2.MORPH_RECT,ksize=(6,6))
dilateimg=cv2.dilate(erodeimg,kernel1,iterations=2)
cv2.imwrite('C:/Users/Lenovo/Desktop/test/A3/3.2.png',dilateimg)

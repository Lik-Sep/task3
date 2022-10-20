import cv2
import numpy as np

img=cv2.imread('C:/Users/Lenovo/Desktop/test/A3/001.3.png')
blurimg=cv2.blur(img,(10,10))
cv2.imwrite('C:/Users/Lenovo/Desktop/test/A3/3.1.1.png',blurimg)

kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
filterimg=cv2.filter2D(blurimg,-1,kernel)
cv2.imwrite('C:/Users/Lenovo/Desktop/test/A3/3.1.png',filterimg)

import cv2
import numpy as np

img=cv2.imread('C:/Users/Lenovo/Desktop/test/B3/image.png',0)

kernel1=np.array(([1/9,1/9,1/9],
                  [1/9,1/9,1/9],
                  [1/9,1/9,1/9]),dtype="float32")
img1=cv2.filter2D(img,-1,kernel1)
cv2.imwrite('C:/Users/Lenovo/Desktop/test/B3/3.2.1.png',img1)

kernel2=np.array(([0,1,0],
                  [1,-4,1],
                  [0,1,0]),dtype="float32")
img2=cv2.filter2D(img,-1,kernel2)
cv2.imwrite('C:/Users/Lenovo/Desktop/test/B3/3.2.2.png',img2)

kernel3=np.array(([-1,-2,-1],
                  [0,0,0],
                  [1,2,1]),dtype="float32")
img3=cv2.filter2D(img,-1,kernel3)
cv2.imwrite('C:/Users/Lenovo/Desktop/test/B3/3.2.3.png',img3)


kernel4=np.array(np.transpose(([-1,-2,-1],
                  [0,0,0],
                  [1,2,1])),dtype="float32")
img4=cv2.filter2D(img,-1,kernel4)
cv2.imwrite('C:/Users/Lenovo/Desktop/test/B3/3.2.4.png',img4)

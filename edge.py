import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('building.jpg')
h=img.shape[0]
w=img.shape[1]
print(h,w)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

lap=cv2.Laplacian(img,cv2.CV_64F)
lap=np.uint8(np.absolute(lap))

sobelX=cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY=cv2.Sobel(img,cv2.CV_64F,0,1)

sobelX=np.uint8(np.absolute(sobelX))
sobelY=np.uint8(np.absolute(sobelY))

sobelC=cv2.bitwise_or(sobelX,sobelY)
titles=['Image','Laplacian','sobelX','sobelY','sobelC']
images=[img,lap,sobelX,sobelY,sobelC]

for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i])
    plt.title(titles[i])

plt.show()
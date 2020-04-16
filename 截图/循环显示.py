import cv2
import numpy as np
import os
from PIL import ImageGrab
#缩放倍数
narrow=1
file=open("coordinate.txt","r")
x1=int(file.readline())
y1=int(file.readline())
x2=int(file.readline())
y2=int(file.readline())
cv2.namedWindow("image",cv2.WINDOW_AUTOSIZE)
for i in range(1000):
    img = ImageGrab.grab((x1*1.25+i,y1*1.25,x2*1.25+i,y2*1.25))
    img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img=cv2.resize(img,(int(img.shape[1]/narrow),int(img.shape[0]/narrow)))
    cv2.imshow("image",img)
    cv2.waitKey(20)
    #print(img)
    #os.system("cls")

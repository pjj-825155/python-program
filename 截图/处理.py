import cv2
import numpy as np
from PIL import ImageGrab
#缩放倍数
narrow=1
#电脑分辨倍数
ratio=1.25
file=open("coordinate.txt","r")
x1=int(file.readline())
y1=int(file.readline())
x2=int(file.readline())
y2=int(file.readline())
#截取照片，转为灰度
img = ImageGrab.grab((x1*ratio,y1*ratio,x2*ratio,y2*ratio))
img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img=cv2.resize(img,(int(img.shape[1]/narrow),int(img.shape[0]/narrow)))
#窗口
cv2.namedWindow("image",cv2.WINDOW_AUTOSIZE)
#去掉模糊化
row,col=img.shape
print(row,col)
for x in range(row):
    for y in range(col):
        if img[x][y]>175:
            img[x][y]=255
        else:
            img[x][y]=0
#确定第一个字符横向范围
char_x_up=0
while char_x_up<row:
    for char_x_up in range(char_x_up,row):
        if (img[char_x_up]==0).any():
            if char_x_up==0:
                break
            if (img[char_x_up-1]==255).all():
                break
    for char_x_down in range(char_x_up,row):
        if (img[char_x_down]==255).all() and (img[char_x_down-1]==0).any():
            break

    char_y_left=0
    #确定第一个字符纵向范围
    while char_y_left<col:
        for char_y_left in range(char_y_left,col):
            if (img[char_x_up:char_x_down,char_y_left]==0).any():
                if char_y_left==0:
                    break
                if (img[char_x_up:char_x_down,char_y_left-1]==255).all():
                    break

        for char_y_right in range(char_y_left,col):
            if (img[char_x_up:char_x_down,char_y_right]==255).all() and (img[char_x_up:char_x_down,char_y_right-1]==0).any():
                break
        if char_x_up<row-1 and char_y_left<col-1:
            print(char_y_left,char_y_right)
            print(char_x_up,char_x_down)

            cv2.imshow("image",img[char_x_up:char_x_down,char_y_left:char_y_right])
            print(img[char_x_up:char_x_down,char_y_left:char_y_right])

        char_y_left+=1
    char_x_up+=1

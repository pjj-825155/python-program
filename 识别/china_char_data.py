import cv2
import numpy as np
from PIL import ImageGrab
import os
#截图
os.system("python get_coor.py")
#缩放倍数
narrow=1
#文件名表
char_name="屏"
char_name=char_name.replace(" ","")
name_num=0
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
#去掉模糊化
row,col=img.shape
#二值化
for x in range(row):
    for y in range(col):
        if img[x][y]>170:
            img[x][y]=1
        else:
            img[x][y]=0
#确定字符横向范围
char_x_up=0
while char_x_up<=row:
    for char_x_up in range(char_x_up,row):
        if (img[char_x_up]==0).any():
            if char_x_up==0:
                break
            if (img[char_x_up-1]==1).all():
                break
    for char_x_down in range(char_x_up,row):
        if (img[char_x_down]==1).all() and (img[char_x_down-1]==0).any():
            break
    char_wide=char_x_down-char_x_up
    print(char_wide)
    #print(img[char_x_up:char_x_down,:])
    char_y_left=0
    #确定字符纵向范围
    while char_y_left<=col:
        for char_y_left in range(char_y_left,col):
            if (img[char_x_up:char_x_down,char_y_left]==0).any():
                if char_y_left==0:
                    break
                if (img[char_x_up:char_x_down,char_y_left-1]==1).all():
                    break
        #框选范围
        char_y_right=char_y_left+int(char_wide*1.25)
        if char_y_right>=col:
            char_y_right=col-1
        for char_y_right in range(char_y_right,char_y_left,-1):
            if (img[char_x_up:char_x_down,char_y_right]==1).all() and (img[char_x_up:char_x_down,char_y_right-1]==0).any():
                break
        #print(char_y_right-char_y_left)
        if char_x_up<row-1 and char_y_left<col-1:
            #横向再过滤
            img_temp=img[char_x_up:char_x_down,char_y_left:char_y_right]
            #print(img_temp)
            img_temp_x,img_temp_y=img_temp.shape
            for img_x_up in range(img_temp_x):
                if (img_temp[img_x_up]==0).any():
                    if img_x_up==0:
                        break
                    if (img_temp[img_x_up-1]==1).all():
                        break
            for img_x_down in range(img_temp_x-1,img_x_up,-1):
                if (img_temp[img_x_down]==0).any():
                    if img_x_down==img_temp_x-1:
                        break
                    if (img_temp[img_x_down+1]==1).all():
                        break
            
            #得到值
            np.savetxt("char_data/char_china_data/"+str(char_name[name_num])+"_data.txt",img_temp[img_x_up:img_x_down,:],fmt='%d')
            name_num+=1
            print(img_temp[img_x_up:img_x_down,:])
        char_y_left=char_y_right+2
    char_x_up=char_x_down+2

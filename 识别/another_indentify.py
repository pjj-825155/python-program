import cv2
import numpy as np
from PIL import ImageGrab
import os

def characteristic(data):
    m,n=data.shape
    vertical=1-np.zeros([(m+2)])
    across=1-np.zeros([n])
    data=np.insert(data,m,across,axis=0)
    data=np.insert(data,0,across,axis=0)
    data=np.insert(data,n,vertical,axis=1)
    data=np.insert(data,0,vertical,axis=1)
    m,n=data.shape
    #记录特征
    #顶点
    origin=0
    #弯曲
    curve=0
    #交叉
    intersect=0
    #判断起点
    #判断弯曲
    #横向
    for x in range(m):
        for y in range(n):
            if data[x,y]==0 and data[x,y-1]==1:
                relay_x,relay_y=x,y
                while not(data[relay_x,relay_y]==0 and data[relay_x,relay_y+1]==1):
                    relay_y+=1
                if (data[x-1,y-1:relay_y+1]==1).all():
                    origin+=1
                    if data[x+1,y-1]==0 or data[relay_x+1,relay_y+1]==0:
                        curve+=1
                    if data[x-1,y-1]==0 or data[relay_x-1,relay_y+1]==0:
                        curve+=1
                if (data[x+1,y-1:relay_y+1]==1).all():
                    origin+=1
                    if data[x+1,y-1]==0 or data[relay_x+1,relay_y+1]==0:
                        curve+=1
                    if data[x-1,y-1]==0 or data[relay_x-1,relay_y+1]==0:
                        curve+=1
    #纵向
    for x in range(m):
        for y in range(n):
            if data[x,y]==0 and data[x-1,y]==1:
                relay_x,relay_y=x,y
                while not(data[relay_x,relay_y]==0 and data[relay_x+1,relay_y]==1):
                    relay_x+=1
                if (data[x-1:relay_x+1,y-1]==1).all():
                    origin+=1
                    if data[x-1,y+1]==0 or data[relay_x+1,relay_y+1]==0:
                        curve+=1
                    if data[x-1,y-1]==0 or data[relay_x+1,relay_y-1]==0:
                        curve+=1
                if (data[x-1:relay_x+1,y+1]==1).all():
                    origin+=1
                    if data[x-1,y+1]==0 or data[relay_x+1,relay_y+1]==0:
                        curve+=1
                    if data[x-1,y-1]==0 or data[relay_x+1,relay_y-1]==0:
                        curve+=1
    #判断交叉
    for x in range(m):
        for y in range(n):
            #向下
            if data[x,y]==0 and data[x+1,y]==1:
                if data[x,y-1]==0 and data[x,y+1]==0 and (data[x+1,y+1]==0 or data[x+1,y-1]==0):
                    intersect+=1
            #向上
            if data[x,y]==0 and data[x-1,y]==1:
                if data[x,y-1]==0 and data[x,y+1]==0 and (data[x-1,y+1]==0 or data[x-1,y-1]==0):
                    intersect+=1
    return origin,curve,intersect

def enlarge(img1,img2):
    img1_x,img1_y=img1.shape
    img2_x,img2_y=img2.shape
    #放大形状
    final_x=img1_x*img2_x
    final_y=img1_y*img2_y
    #生成两个新矩阵
    array_img1=np.zeros((final_x,final_y))
    array_img2=np.zeros((final_x,final_y))
    for m in range(img1_x):
        for n in range(img1_y):
            array_img1[m*img2_x:(m+1)*img2_x,n*img2_y:(n+1)*img2_y]=img1[m,n]

    for m in range(img2_x):
        for n in range(img2_y):
            array_img2[m*img1_x:(m+1)*img1_x,n*img1_y:(n+1)*img1_y]=img2[m,n]
            
    return array_img1,array_img2
    
def get_value(img):
    global oci
    img_x,img_y=img.shape
    file_list=open("char_data/file_list.txt","r")
    file_name=file_list.readline()
    max_per=0
    max_value=""
    #特征
    if oci:
        img_origin,img_curve,img_intersect=characteristic(img)
    while file_name:
        file_name=file_name.strip("\n")
        data_list=open("char_data/"+file_name+"/data_list.txt","r")
        data_name=data_list.readline()
        while data_name:
            data_name=data_name.strip("\n")
            #获取样例数据
            char_data=np.loadtxt("char_data/"+file_name+"/"+data_name+"_data.txt",skiprows=0,dtype=int)
            #特征
            if oci:
                data_origin,data_curve,data_intersect=characteristic(char_data)
                #权值，顶点4，弯曲3，交叉3
                origin_value,curve_value,intersect_value=0,0,0
                if img_origin==data_origin+1 or img_origin==data_origin-1:
                    origin_value=4
                if img_curve==data_curve+1 or img_curve==data_curve-1:
                    curve_value=3
                if img_intersect==data_intersect+1 or img_intersect==data_intersect-1:
                    intersect_value=3
            char_data_x,char_data_y=char_data.shape
            #样例放大
            char_data,img_temp=enlarge(char_data,img)
            final=cv2.absdiff(char_data,img_temp)
            #累加
            var=np.cumsum(final)
            #求百分比
            #权值，对比7，特征3
            if oci:
                per=(1-var[-1]/(final.shape[0]*final.shape[1]))*0.7+((origin_value+curve_value+intersect_value)/100)*0.3
            else:
                per=1-var[-1]/(final.shape[0]*final.shape[1])
            if per>max_per:
                max_per=per
                max_value=data_name
            data_name=data_list.readline()
        file_name=file_list.readline()
    print(max_value,end="")
    return max_value
    

#截图
os.system("python get_coor.py")
#缩放倍数
narrow=1
#特征
oci=0
#电脑分辨倍数
ratio=1.25
#字体大小
char_length=0
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
for x in range(row):
    for y in range(col):
        if img[x][y]>175:
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
    char_y_left=0
    #确定字符纵向范围
    while char_y_left<=col:
        for char_y_left in range(char_y_left,col):
            if (img[char_x_up:char_x_down,char_y_left]==0).any():
                if char_y_left==0:
                    break
                if (img[char_x_up:char_x_down,char_y_left-1]==1).all():
                    break

        for char_y_right in range(char_y_left,col):
            if (img[char_x_up:char_x_down,char_y_right]==1).all() and (img[char_x_up:char_x_down,char_y_right-1]==0).any():
                break
        if char_x_up<row-1 and char_y_left<col-1:
            #横向再过滤
            img_temp=img[char_x_up:char_x_down,char_y_left:char_y_right]
            img_temp_x,img_temp_y=img_temp.shape
            for img_x_up in range(img_temp_x):
                if (img_temp[img_x_up]==0).any():
                    if img_x_up==0:
                        break
                    if (img_temp[img_x_up-1]==1).all():
                        break
            for img_x_down in range(img_temp_x-1,img_x_up-1,-1):
                if (img_temp[img_x_down]==0).any():
                    if img_x_down==img_temp_x-1:
                        break
                    if (img_temp[img_x_down+1]==1).all():
                        break
            
            #得到值
            char_value=get_value(img_temp[img_x_up:img_x_down,:])
            #确认间距，写空格
            if char_length!=0:
                char_length=(char_length+char_y_right-char_y_left)/2
            else:
                char_length=char_y_right-char_y_left
                
            if (img[char_x_up:char_x_down,char_y_right:char_y_right+int(char_length*0.625)]==1).all():
                print(" ",end="")
        char_y_left+=1
    print()
    char_x_up+=1

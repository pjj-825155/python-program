import cv2
import numpy as np

#data=np.loadtxt("char_lowletter_data/k_data.txt",skiprows=0,dtype=int)
#data=np.loadtxt("char_number_data/0_data.txt",skiprows=0,dtype=int)
data=np.loadtxt("char_symbol_data/$_data.txt",skiprows=0,dtype=int)
#判定顶点
m,n=data.shape
vertical=255-np.zeros([(m+2)])
across=255-np.zeros([n])
data=np.insert(data,m,across,axis=0)
data=np.insert(data,0,across,axis=0)
data=np.insert(data,n,vertical,axis=1)
data=np.insert(data,0,vertical,axis=1)
m,n=data.shape
#记录特征
origin=0
curve=0
intersect=0
#判断起点
#判断弯曲
#横向
for x in range(m):
    for y in range(n):
        if data[x,y]==0 and data[x,y-1]==255:
            relay_x,relay_y=x,y
            while not(data[relay_x,relay_y]==0 and data[relay_x,relay_y+1]==255):
                relay_y+=1
            if (data[x-1,y-1:relay_y+1]==255).all():
                origin+=1
                if data[x+1,y-1]==0 or data[relay_x+1,relay_y+1]==0:
                    curve+=1
                if data[x-1,y-1]==0 or data[relay_x-1,relay_y+1]==0:
                    curve+=1
            if (data[x+1,y-1:relay_y+1]==255).all():
                origin+=1
                if data[x+1,y-1]==0 or data[relay_x+1,relay_y+1]==0:
                    curve+=1
                if data[x-1,y-1]==0 or data[relay_x-1,relay_y+1]==0:
                    curve+=1
#纵向
for x in range(m):
    for y in range(n):
        if data[x,y]==0 and data[x-1,y]==255:
            relay_x,relay_y=x,y
            while not(data[relay_x,relay_y]==0 and data[relay_x+1,relay_y]==255):
                relay_x+=1
            if (data[x-1:relay_x+1,y-1]==255).all():
                origin+=1
                if data[x-1,y+1]==0 or data[relay_x+1,relay_y+1]==0:
                    curve+=1
                if data[x-1,y-1]==0 or data[relay_x+1,relay_y-1]==0:
                    curve+=1
            if (data[x-1:relay_x+1,y+1]==255).all():
                origin+=1
                if data[x-1,y+1]==0 or data[relay_x+1,relay_y+1]==0:
                    curve+=1
                if data[x-1,y-1]==0 or data[relay_x+1,relay_y-1]==0:
                    curve+=1
#判断交叉
for x in range(m):
    for y in range(n):
        #向下
        if data[x,y]==0 and data[x+1,y]==255:
            if data[x,y-1]==0 and data[x,y+1]==0 and (data[x+1,y+1]==0 or data[x+1,y-1]==0):
                intersect+=1
        #向上
        if data[x,y]==0 and data[x-1,y]==255:
            if data[x,y-1]==0 and data[x,y+1]==0 and (data[x-1,y+1]==0 or data[x-1,y-1]==0):
                intersect+=1

print(origin)
print(curve)
print(intersect)              
print(data)

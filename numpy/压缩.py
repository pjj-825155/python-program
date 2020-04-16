import numpy as np

data=np.loadtxt("0_data.txt",skiprows=0,dtype=int)
x,y=data.shape
x-=1
y-=1
print(data)
for m in range(1,x):
    for n in range(y):
        #顶不变,尾不变
        #255-255-255=255
        #0-255-255=255
        #255-255-0=0
        #0-255-0=255
        
        #0-0-0=0
        #0-0-255=255
        #255-0-0=0
        #255-0-255=0
        if data[m][n]==255 and data[m-1][n]==255 and data[m+1][n]==0:
            data[m][n]=0
        if data[m][n]==0 and data[m-1][n]==0 and data[m+1][n]==255:
            data[m][n]=255
data=data[0:x-1][:]
print(data)

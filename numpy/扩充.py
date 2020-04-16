import numpy as np

data=np.loadtxt("0_data.txt",skiprows=0,dtype=int)
x,y=data.shape
att=255-np.zeros(y)
x-=1
y-=1
print(data)
print(att)
data=np.vstack((data,att))
print(data)

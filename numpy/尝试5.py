import numpy as np

a=np.arange(12).reshape(3,4)
print(a)

print(np.split(a,2,axis=1))#纵向分割成两部分
print(np.split(a,3,axis=0))#横向分割成两部分

#不等量分割
print(np.array_split(a,3,axis=1))
#纵向分割
print(np.vsplit(a,3))
#横向分割
print(np.hsplit(a,2))

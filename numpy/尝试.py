import numpy as np
#np.int32(默认) np.int64||np.float32 np.float64(默认)
array=np.array([[1,2,3],[4,5,6]],dtype=np.int)
print(array)
#输出类型
print(array.dtype)
#输出维度
print(array.ndim)
#输出形状
print(array.shape)
#输出大小
print(array.size)
#生成一个全是0的矩阵
a=np.zeros((3,4))
print(a)
#生成一个顺序数列
b=np.arange(10,20,1)
print(b)
#生成一个顺序矩阵
c=np.arange(12).reshape((3,4))
print(c)
#分段生成
d=np.linspace(1,10,5)
print(d)
d=np.linspace(1,10,6).reshape((2,3))
print(d)

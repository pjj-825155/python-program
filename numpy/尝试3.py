import numpy as np

a=np.arange(3,15).reshape(3,4)

print(a)
#第一行所有
print(a[1,:])
#第一列所有
print(a[:,1])
#第一行的一到三列
print(a[1,1:3])
#多维转为一维
print(a.flatten())
#转置后输出每一列
for col in a.T:
    print(col)

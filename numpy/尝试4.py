import numpy as np

a=np.array([1,1,1])
b=np.array([2,2,2])
#上下合并
c=np.vstack((a,b))
print(c)
#左右合并
d=np.hstack((a,b))
print(d)
print(a.shape,c.shape,d.shape)
#横向改为纵向
print(a[:,np.newaxis])
#改为纵向后合并
a=a[:,np.newaxis]
b=b[:,np.newaxis]
d=np.hstack((a,b))
print(d)
#多个合并
c=np.concatenate((a,b,b,a),axis=0)#纵向
print(c)
c=np.concatenate((a,b,b,a),axis=1)#横向
print(c)

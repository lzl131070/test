import numpy as np
d = np.array([-1, 0, 1, 2, -1, -4])
n1 = np.array([-1, 0, 1, 2, -1, -4]).reshape((1,1,-1))
n2 = np.array([-1, 0, 1, 2, -1, -4]).reshape((1,-1,1))
n3 = np.array([-1, 0, 1, 2, -1, -4]).reshape((-1,1,1))
n = n1+n2+n3
l = np.argwhere(n==0)
l2 = l[l[:,2]>l[:,1]]
n3 = l2[l2[:,1] > l2[:,0]]
print(d[n3])
# [[0 1 2]
#  [0 3 4]
#  [1 2 4]]
# def fn(l=[-1, 0, 1, 2, -1, -4]):

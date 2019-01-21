def fnumpy(d=[-1, 0, 1, 2, -1, -4]):
    import numpy as np
    d = np.array(d)
    n1 = d.reshape((1,1,-1))
    n2 = d.reshape((1,-1,1))
    n3 = d.reshape((-1,1,1))
    n = n1+n2+n3
    l = np.argwhere(n==0)
    l2 = l[l[:,2]>l[:,1]]
    n3 = l2[l2[:,1] > l2[:,0]]
    res = np.unique(np.sort(d[n3]),axis=0)
    return res

def fn(l=[-1, 0, 1, 2, -1, -4]):
    x = len(l)
    res = []
    for i in range(x):
        a = l[i]
        for j in range(i+1,x):
            b = l[j]
            for k in range(j+1,x):
                c = l[k]
                if a + b + c == 0 and sorted([a,b,c]) not in res:
                    res.append(sorted([a,b,c]))
    return res
if __name__ == '__main__':

    print(fnumpy())
    print(fn())


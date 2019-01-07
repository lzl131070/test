import numpy as np
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
class Num(object):
    def __init__(self,list,num):
        self.list=list
        self.num=num
    def fn(self):
        res = []
        for i in self.list:

            for j in self.list[self.list.index(i)+1:]:
                if i+j==self.num:
                    res.append([self.list.index(i),self.list.index(j)])
        return res


if __name__ == '__main__':
    a = Num([1, 2, 3, 4, 5, 7, 8, 9], 10)
    print(a.fn())

    # numpy way
    n1 = np.array([1, 2, 3, 4, 5, 7, 8, 9])
    n2 = n1.reshape((-1,1))
    n3 = n1 + n2
    l = np.argwhere(n3==10)
    print(l[l[:,0]<l[:,1]])
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
class Num(object):
    def __init__(self,list,num):
        self.list=list
        self.num=num
    def fn(self):
        for i in self.list:
            for j in self.list:
                if i!=j and i+j==self.num:
                    return self.list.index(i),self.list.index(j)


def main():
    a=Num([1,2,3,4,5,7,8,9],10)
    print(a.fn())

if __name__ == '__main__':
    main()
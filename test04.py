class Solution:
    def __init__(self,list1,list2):
        self.list1=list1
        self.list2=list2
    def fn(self):
        listn=self.list1+self.list2
        listc=listn[:]
        listnum=[]
        while listc!=[]:
            a=min(listc)
            listc.remove(a)
            listnum.append(a)
        num=len(listn)
        if num%2==0:
            a=listnum[num//2-1]+listnum[num//2]
            a=a/2
        else:
            a=listnum[num//2]
        return a
def main():
    a=Solution([1,2,4],[1,2,3,8])
    print(a.fn())

if __name__ == '__main__':
    main()
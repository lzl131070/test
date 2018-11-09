class Solution:
    def __init__(self,str,n):   #   "PAYPALISHIRING",3
        self.n=n
        self.str=str
    def los(self):
        los=self.n-1   #每个小组的列数 2
        lenth = len(self.str)
        b=lenth//Solution.num(self)
        a=lenth%Solution.num(self)  # 不够造成整租的数量

        if 0<a<self.n:
            losnum=los*b+1
        else:
            losnum=los*b+a-self.n+1
        return losnum
    def num(self):
        num=2*self.n-2
        return num     #    每个小组的字母数 4
    def echoStr(self):
        lenth=len(self.str)
        cow=lenth//self.n+1
        for i in range(self.n):
            for k in range(lenth):
                if i==0 or i==self.n-1:
                    if k%Solution.num(self)==i:
                        print(self.str[k],end="\t \t")
                else:
                    if k%(i+1)==i:
                        print(self.str[k],end="\t")
            print()


if __name__ == '__main__':
    aa=Solution("PAYPALISHIRING",3)
    aa.echoStr()


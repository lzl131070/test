class Solution:
    def __init__(self,num):
        self.num=num

    def theNum(self):

        theA=1
        n=0
        newNum=0
        c=self.num*1
        if self.num<0:
            return False
        while self.num//theA!=0:
            n += 1
            theA=10**n
        for i in range(n):

            a=self.num//(10**(n-1-i))
            if i==n-1:
                a=self.num%10
            # c+=10**a
            b=a*10**i
            self.num-=a*10**(n-1-i)
            newNum+=b
        if newNum==c:
            return True
        return False
if __name__ == '__main__':
    aa=Solution(111)
    print(aa.theNum())
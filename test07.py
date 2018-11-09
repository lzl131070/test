class Solution:
    def __init__(self,num):
        self.num=num
    def fn(self):
        if self.num>0:
            num=str(self.num)
            num=num[::-1]
            num=int(num)
        else:
            num=-self.num
            num = str(num)
            num = num[::-1]
            num = int(num)
            num=-num
        return num
if __name__ == '__main__':
    a=Solution(-120)
    print(a.fn())

class Solution:
    def __init__(self,num):
        self.num=num

    def fn(self):
        stra=""
        listRoma=["I","V","X","L","C","D","M"]
        listnum=[1,5,10,50,100,500,1000]
        for j in range(7):
            num_a=self.num-listnum[j]
            if num_a<0 and -num_a in listnum and listnum[j]/(-num_a)!=2:
                b=listRoma[listnum.index(-num_a)]+listRoma[j]
                return b

        for i in range(7):

            theA = self.num // listnum[6 - i]
            self.num = self.num % listnum[6 - i]

            stra+=theA*listRoma[6-i]
        return stra

if __name__ == '__main__':
    a=Solution(50)
    print(a.fn())

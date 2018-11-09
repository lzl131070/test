# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
''''''
"""
0,1
1,8
2,6
3,2
4,5
5,4
6,8
7,3
8,7   
49

(i2-i1)*min(list[i2],list[i1])
"""
class Solution:
    def __init__(self,list):
        self.list=list

    def fn(self):
        listS=[]
        for i in range(len(self.list)-1):
            for j in range(i+1,len(self.list)):
                s=(j-i)*min(self.list[i],self.list[j])
                listS.append(s)
        return max(listS)

if __name__ == '__main__':

    a=Solution([1,8,6,2,5,4,8,3,7])
    print(a.fn())
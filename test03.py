class Solution:
    def __init__(self,str):
        self.str=str
    def fn(self):
        theStr=""
        listnum=[]
        listStr=[]
        for i in range(len(self.str)):

            theStr = self.str[i]
            for k in range(i+1,len(self.str)):
                j=self.str[k]
                if j not in theStr:
                    theStr+=j
                else:
                    listnum.append(len(theStr))
                    listStr.append(theStr)
                    break
        return max(listnum),listStr
def main():
    a=Solution("xfhtydrxxaffgjvb")
    print(a.fn())


if __name__ == '__main__':
    main()
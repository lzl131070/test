class Solution:
    def __init__(self,str):
        self.str=str
    def fn(self):
        theStr=self.str
        listNum=[]
        for i in range(len(theStr)):
            a=theStr[i]
            for j in range(i+1,len(theStr)):
                j=theStr[j]
                a+=j
                b=len(a)
                for k in range(b//2):
                    if a[k]==a[b-k-1]:
                        pass
                    else:
                        break
                    if k==b//2-1:

                        listNum.append(a)
        return listNum


def main():
    a=Solution("asdfnzsfafsfafsssssdddsfwefv")
    print(a.fn())
    listmain={}
    for i in a.fn():
        listmain[i]=len(i)
    print(listmain)
    print(max(listmain.values()))
if __name__ == '__main__':
    main()
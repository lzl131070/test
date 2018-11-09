class Solution:
    def __init__(self,str,listWord):
        self.str=str
        self.listWord=listWord

    def fn(self):
        listnum=[]
        for i in self.listWord:
            numa=-1
            numb=0
            n=0
            for j in range(len(i)):
                try:
                    numb=self.str.index(i[j])
                    if numb>numa:
                        numa=numb
                        n+=1
                except:
                    break
                if n == len(i):
                    listnum.append(i)
        return len(listnum),listnum
if __name__ == '__main__':
    a=Solution("abcde",["a", "bb", "acd", "ace","ba"])
    print(a.fn())
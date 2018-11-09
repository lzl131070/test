class Solution:
    def __init__(self,str):
        self.str=str
    def fn(self):
        theStr=self.str
        numStr=""
        while theStr[0] is " ":
            theStr=theStr[1:]
        if theStr[0].isalpha:
            return 0
        while theStr[0].isdigit():
            numStr+=theStr[0]
            theStr=theStr[1:]

        return numStr

if __name__ == '__main__':
    aa=Solution("a  45154adsga")
    print(aa.fn())

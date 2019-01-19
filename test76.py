'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
'''
def fn(s1='ADOBECODEBANC', s2='ABC'):
    s = ''
    l = len(s1)
    for i in range(len(s1)):
        for j in range(i+1,len(s1)):
            m = 0
            for n in range(len(s2)):
                if s2[n] in s1[i:j+1]:
                    m += 1
            if m == len(s2) and len(s1[i:j+1]) < l:
                s = s1[i:j+1]
                l = len(s1[i:j+1])
    return s,l

if __name__ == '__main__':
    print(fn())
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
# Input: ["flower","flow","flight"]
# Output: "fl"
def fn(l=["flower","flow","flight"]):
    s = ':'+':'.join(l)
    d = l[0]
    for i in range(len(d)):
       if s.count(':'+ d[:i]) != len(l):
           return d[:i-1]

    return ''

if __name__ == '__main__':
    print(fn(["dog","racecar","car"]))
    print(fn())
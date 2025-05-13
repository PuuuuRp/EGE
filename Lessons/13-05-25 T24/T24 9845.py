from re import *
with open('24_9845.txt') as f:
    st = f.readline()
pat = r'([ABC][89])+[ABC]?|([89][ABC])+[89]?'
m = [i.group() for i in finditer(pat, st)]

print(max(m, key=len))
print(len(max(m, key=len)))
#
from re import *
with open('24_6636.txt') as f:
    st = f.readline()
pat = r'([24][135])+'
m = [i.group() for i in finditer(pat, st)]

print(len(max(m, key=len))//2)
#10
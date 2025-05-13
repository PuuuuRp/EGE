from re import *
with open('24_3228.txt') as f:
    st = f.readline()

pat = r'(AC|AB)+'
m = [i.group() for i in finditer(pat, st)]

print(max(m, key=len))
print(len(max(m, key=len))//2)
#19
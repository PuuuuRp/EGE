from re import *
with open('24_4602 (1).txt') as f:
    st = f.readline()
pat = r'([BCD][AO])+'
m = [i.group() for i in finditer(pat, st)]

print(max(m, key=len))
print(len(max(m, key=len))//2)
#174
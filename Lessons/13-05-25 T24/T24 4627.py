from re import *
with open('24_4627.txt') as f:
    st = f.readline()
pat = r'(NPO|PNO)+'
m = [i.group() for i in finditer(pat, st)]

print(max(m, key=len))
print(len(max(m, key=len))//3)
#327
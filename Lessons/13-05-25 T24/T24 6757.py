from re import *
with open('24_6757.txt') as f:
    st = f.readline()
pat = r'(CFE|FCE)+'
m = [i.group() for i in finditer(pat, st)]

print(max(m, key=len))
print(len(max(m, key=len))//3)
#103
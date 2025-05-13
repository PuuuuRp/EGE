from re import *
with open('24_2942.txt') as f:
    st = f.readline()
pat = r'(AB|AC)+'
m = [i.group() for i in finditer(pat, st)]

print(max(m, key=len))
print(len(max(m, key=len))//2)
#2397
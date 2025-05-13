from re import *
with open('24_6054.txt') as f:
    st = f.readline()
pat = r'([BC][BC][A])+'
m = [i.group() for i in finditer(pat, st)]

print(len(max(m, key=len)))
#6
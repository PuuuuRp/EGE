from re import *
with open('24_4643.txt') as f:
    st = f.readline()
pat = r'(\d{2}[AB])+'
m = [i.group() for i in finditer(pat, st)]

print(max(m, key=len))
print(len(max(m, key=len))//3)
#67
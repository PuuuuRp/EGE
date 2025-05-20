from re import *
with open('24_21421.txt') as f:
    st = f.readline()

pat = r'[1-9][0-9AB]+[02468A]'
m = [i.group() for i in finditer(pat, st)]

print(max(m, key=len))
print(len(max(m, key=len)))
#19
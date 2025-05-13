from re import *
with open('24_9791.txt') as f:
    st = f.readline()
pat = r'[1-9A-F][0-9A-F]+'
m = [i.group() for i in finditer(pat, st)]

print(max(m, key=len))
print(len(max(m, key=len)))
#21
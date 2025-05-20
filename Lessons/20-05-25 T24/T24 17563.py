from re import *
with open('24_17563.txt') as f:
    st = f.readline()

pat = r'[1-9]\d*([-*][1-9]\d*)+'
m = [i.group() for i in finditer(pat, st)]

print(max(m, key=len))
print(len(max(m, key=len)))
#40
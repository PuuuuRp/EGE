from re import *
with open('24_20813.txt') as f:
    st = f.readline()

pat = r'([1-9]\d*|0)([-*]([1-9]\d*|0))+'
m = [i.group() for i in finditer(pat, st)]

print(max(m, key=len))
print(len(max(m, key=len)))
#111
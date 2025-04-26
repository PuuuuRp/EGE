from re import *
with open('24_332.txt') as f:
    st = f.readline()

pat = r'[ABC][abc]*( [ABC]?[abc]+)+\.'
m = [i.group() for i in finditer(pat, st)]

print(max(m, key=len))
print(len(max(m, key=len)))
#22
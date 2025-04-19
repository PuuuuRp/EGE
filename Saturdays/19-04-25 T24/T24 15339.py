from re import *
with open('24_15339.txt') as f:
    st = f.readline()

pattern  = r'(\d[ABC])+\d?|([ABC]\d)+[ABC]?'
m = [i.group() for i in finditer(pattern, st)]
print(len(max(m, key=len)))
print(max(m, key=len))
#22
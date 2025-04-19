from re import *
with open('24_18597.txt') as f:
    st = f.readline()

pattern  = r'[1-9]\d{3}\.\d+\&[1-9]\d{3}\.\d+'
m = [i.group() for i in finditer(pattern, st)]
print(len(max(m, key=len)))
print(max(m, key=len))
#45
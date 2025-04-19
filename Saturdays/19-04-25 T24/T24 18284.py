from re import *
with open('24_18284.txt') as f:
    st = f.readline()

pattern  = r'L[^L]*?O.*?V.*?E'
m = [i.group() for i in finditer(pattern, st)]
print(len(max(m, key=len)))
#print(max(m, key=len))
#2000031
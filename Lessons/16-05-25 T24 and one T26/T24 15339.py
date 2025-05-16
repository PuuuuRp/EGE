from re import *
with open('24_15339 (1).txt') as f:
    st = f.readline()
pat = r'(\d\D)+\d?|(\D\d)+\D?'
m = [i.group() for i in finditer(pat, st)]

print(max(m, key=len))
print(len(max(m, key=len)))
#22
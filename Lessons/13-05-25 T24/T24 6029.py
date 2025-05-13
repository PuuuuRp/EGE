from re import *
with open('24_6029.txt') as f:
    st = f.readline()
pat = r'(EF)+E?|(FE)+F?'
m = [i.group() for i in finditer(pat, st)]

print(len(max(m, key=len)))
print(max(m, key=len))
#11
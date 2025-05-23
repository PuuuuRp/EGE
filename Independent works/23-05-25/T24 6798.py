from re import *
with open('24_6798.txt') as f:
    st  = f.readline()

pat  = r'([CDF]\D[AO])+'
m = [i.group() for i in finditer(pat, st)]

print(max(m, key=len))
print(len(max(m, key=len))/3)
#6
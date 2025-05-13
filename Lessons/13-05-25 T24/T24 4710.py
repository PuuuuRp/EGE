from re import *
with open('24_4710.txt') as f:
    st = f.readline()
pat = r'([AO][CDF])+'
m = [i.group() for i in finditer(pat, st)]

print(len(max(m, key=len))//2)
#95
from re import *
with open('24_12254.txt') as f:
    st = f.readline()

pat1 = r'(SQ)?(RSQ)+(RS)?'
pat2 = r'Q?(RSQ)+(RS)?'
pat3 = r'(SQ)?(RSQ)+R?'
pat4 = r'Q?(RSQ)+R?'
m = [i.group() for i in finditer(pat1, st)]
m += [i.group() for i in finditer(pat2, st)]
m += [i.group() for i in finditer(pat3, st)]
m += [i.group() for i in finditer(pat4, st)]

print(max(m, key=len))
print(len(max(m, key=len)))
#54
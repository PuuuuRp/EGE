from re import *
with open('24_4627.txt') as f:
    st = f.readline()

pattern = r'(NPO|PNO)+'
match = finditer(pattern, st)
m = [i.group() for i in match]
print(len(max(m, key=len))/3)
#327
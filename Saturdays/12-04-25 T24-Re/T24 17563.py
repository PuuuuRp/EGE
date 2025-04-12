from re import *
with open('24_17563.txt') as f:
    st = f.readline()

pattern = r'([789][0789]*[-*])+'
match = finditer(pattern, st)
m = [i.group() for i in match]
print(len(max(m, key=len)))
print(max(m, key=len))
#40
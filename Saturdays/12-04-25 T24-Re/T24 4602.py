from re import *
with open('24_4602.txt') as f:
    st = f.readline()
pattern = r'([BCD][AO])+'
match = finditer(pattern, st)
m = [i.group() for i in match]
print(len(max(m, key=len))//2)
#174
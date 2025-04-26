from re import *
with open('24_337.txt') as f:
    st = f.readline()

pat = r'1[0-9ABCD]+'
m = [i.group() for i in finditer(pat, st)]

res = 0
for i in m:
    for x in range(len(i)-1):
        if i[x]!='1': continue
        for y in range(x+1, len(i)):
            if int(i[x:y+1], 14)%7==0:
                res = max(res, len(i[x: y+1]))
print(res)
#71
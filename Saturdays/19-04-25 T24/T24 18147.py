from re import *
with open('24_18147.txt') as f:
    st = f.readline()

pattern  = r'\d+(\+\d+)+'
m = [i.group() for i in finditer(pattern, st)]
res = 0
for i in m:
    res = max(res, eval(i))
print(res)
#9988877898985
from itertools import *

with open('9_4614.txt') as f:
    arr = [list(map(int, i.split())) for i in f.readlines() if i]

c = 0
for i in arr:
    u1 = max(i) < sum(i) - max(i)
    u2 = len(i) - len(set(i)) == 1
    if u1 and u2:
        c += 1
print(c)
#138
from itertools import *

with open('9_4589.txt') as f:
    arr = [list(map(int, i.split())) for i in f.readlines() if i]

def u2(arr):
    for val in permutations(arr):
        if sum(val[:2]) == sum(val[2:]):
            return True
    return False

c = 0
for i in arr:
    u1 = max(i) < sum(i) - max(i)
    if u1 and u2(i):
        c += 1
print(c)
#104
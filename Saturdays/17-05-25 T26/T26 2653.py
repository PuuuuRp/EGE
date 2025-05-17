from itertools import *
with open('26_2653.txt') as f:
    N = int(f.readline())
    arr = [int(i) for i in f if i]

arr = sorted(arr)
s = sum(arr)
nums = set()
for x in range(1, N):
    for i in combinations(arr, x):
        i = sum(i)
        nums |= {s-i}

nums = list(nums)
res = []
for i in range(len(nums)-1):
    p = nums[i: i+2]
    if p[1]-p[0]>1:
        for x in range(p[0]+1, p[1]):
            res.append(x)
print(len(res), max(res))
#
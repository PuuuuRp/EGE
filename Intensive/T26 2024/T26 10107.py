with open('26_10107.txt') as f:
    N = int(f.readline())
    arr = [list(map(int, i.split())) for i in f if i]

arr = sorted(arr, key=lambda x: x[1])
res = [arr[0][1]]
last_st = 0
for st, fn in arr[1:]:
    if st - res[-1]>=0:
        res.append(fn)

arr = sorted(arr, key=lambda x: -x[0])
ans = []
for st, fn in arr:
    ans.append(st-res[-2])
print(len(res), max(ans))
#32 15
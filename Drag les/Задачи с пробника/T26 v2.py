with open('26v2.txt') as f:
    N = int(f.readline())
    arr = [list(map(int, i.split())) for i in f if i]
arr = sorted(arr)[::-1]

res = []
for day in range(max(arr, key=lambda x: x[0])[0], 0, -1):
    c_res = []
    for x in arr:
        if x[0] >= day:
            c_res.append(x)
    m = max(c_res, key=lambda x: x[1])
    res.append(m[1])
    arr.pop(arr.index(m))
print(sum(res), min(res))
#249966 617
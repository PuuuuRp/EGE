with open('26_17643.txt') as f:
    N = int(f.readline())
    arr = [list(map(int, i.split())) for i in f if i]

arr = sorted(arr, key=lambda x: (-x[1], -x[2], -x[0]))
rich = sum(i[1] for i in arr)/N
id = []
for i in arr.copy():
    if i[1]>=rich:
        id.append(i[0])

res = []
for i in set(id):
    cnt_1 = 0
    cnt_0 = 0
    p = 0
    for idd, pr, st in arr:
        if i == idd:
            p = pr
            if st==1: cnt_1 += 1
            else: cnt_0 += 1
    res.append([i, cnt_0, p, cnt_1, cnt_0*p])

res = sorted(res, key=lambda x: (-x[1], -x[2], x[3]))
print(res[0])
#43656 36
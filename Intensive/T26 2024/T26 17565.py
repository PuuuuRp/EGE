with open('26_17565.txt') as f:
    N, S = map(int, f.readline().split())
    d = [list(map(int, i.split())) for i in f if i]

arr = []
for id, _1, _2, _3, c in d:
    arr.append([_1+_2+_3, c, id])

arr = sorted(arr, key=lambda x: (-x[0], -x[1], x[2]))
res = []
for i in arr[:S]:
    res.append(i)
print(res[-10:]) #7600410

cnt = 0
for i in arr:
    if i[0] == min(res, key=lambda x: x[0])[0]:
        cnt += 1
print(cnt)
#7600410 14
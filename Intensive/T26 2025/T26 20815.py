with open('26_20815.txt') as f:
    n, k = map(int, f.readline().split())
    d = [list(map(int, i.split())) for i in f if i]

arr = []
for id, _1, _2, _3, sob in d:
    arr.append([_1+_2+_3+sob, sob, id])
arr = sorted(arr, key=lambda x: (-x[0], -x[1], x[2]))

res = []
for i in arr[:k]:
    res.append(i)

prohod= res[-1][0]
for i in res[::-1]:
    if prohod != i[0]:
        prohod = i[2]
        break

cnt = 0
for i in arr:
    if res[-1][0] == i[0]:
        cnt += 1
print(prohod, cnt)
#45539 127
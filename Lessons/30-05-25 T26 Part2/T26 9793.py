with open('26_9793.txt') as f:
    N = int(f.readline())
    d = [list(map(int, i.split())) for i in f if i]

arr = []
cnt = 1
for i in d:
    arr.append([cnt, i[0], i[1]])
    cnt += 1

arr = sorted(arr, key=lambda x: (x[2] + x[1]))
res1 = []
res2 = []
last = 0
for n, sh, col in arr:
    if min(sh, col) == sh:
        res1.append([n, sh, 1])
        last = [n, sh, 1]
    else:
        res2.append([n, col, 2])
        last = [n, col, 2]

res = res1 + res2
cnt = 0
for i in res[:res.index(last)]:
    if i[2] == 1:
        cnt += 1
print(last[0], cnt)
#895 488
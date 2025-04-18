with open('26_2651.txt') as f:
    N = int(f.readline())
    arr = [list(map(int, i.split())) for i in f if i]

arr = sorted(arr, key=lambda x: -x[0])

res = []
col = set()
last = arr[0][0]
for i in range(len(arr)):
    if arr[i][0] != last:
        res.append([last, 8-len(col)])
        last = arr[i][0]
        col = set()
    col |= {arr[i][1]}
res.append([last, 8-len(col)])

res = sorted(res, key=lambda x: (-x[1], -x[0]))
print(sum(i[1] for i in res), res[0][0])
#38 1985
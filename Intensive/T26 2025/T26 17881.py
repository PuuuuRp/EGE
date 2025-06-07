with open('26_17881.txt') as f:
    N = int(f.readline())
    arr = [list(map(int, i.split())) for i in f if i]

arr = sorted(arr, key=lambda x: (-((x[1]+x[2]+x[3]+x[4])/4), x[0]))

res = []
_2 = []
for i in arr:
    if 2 not in i:
        res.append(i)
    else:
        _2.append(i)
res += _2

for i in res:
    if i[1:].count(2) > 2:
        print(res[N//4-1][0], i[0])
        break
#52326 635
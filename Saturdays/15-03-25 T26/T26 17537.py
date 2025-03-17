with open('26_17537.txt') as f:
    N, M, K = map(int, f.readline().split())
    arr = [list(map(int, i.split())) for i in f.readlines() if i]
arr = sorted(arr, key=lambda x: (x[1], -x[0]))
opora = [M+1]*(K+1)
for r, m in arr:
    opora[m] = r

res = []
for i in range(1, len(opora)-1):
    r1, r2 = opora[i: i+2]
    res.append([min(r1, r2)-1, i+1])
res = sorted(res, key=lambda x: (-x[0], -x[1]))
print(res[0])
#9991 5643
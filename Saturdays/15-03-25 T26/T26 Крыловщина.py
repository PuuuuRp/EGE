with open('26var01.txt') as f:
    N, M, K = map(int, f.readline().split())
    arr = [list(map(int, i.split())) for i in f.readlines() if i]
arr = sorted(arr, key=lambda x: (x[1], -x[0]))

opora = [0]*(K+1)
for i in arr:
    opora[i[1]] = i[0]

res = []
for mesto in range(1, len(opora)-1):
    pot = opora[mesto: mesto+2]
    res.append([min(pot)-1, mesto])
res = sorted(res, key=lambda x: (-x[0], x[1]))
print(res[0])
#1952 2364
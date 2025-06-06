with open('26_17537.txt') as f:
    N, M, K = map(int, f.readline().split())
    arr = [list(map(int, i.split())) for i in f if i]

res = [10**6]*(K+1)
for i in range(1, len(res)):
    for r, m in arr:
        if i==m:
            res[i] = min(res[i], r-1)

ans = []
for i in range(1, len(res)-1):
    m1, m2 = res[i: i+2]
    if m1<m2:
        ans.append([m1, i+1])
    else:
        ans.append([m2, i+1])
print(max(ans))
#9991 5643
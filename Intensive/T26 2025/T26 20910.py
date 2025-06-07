with open('26_20910.txt') as f:
    n, m, k = map(int, f.readline().split())
    arr = [list(map(int, i.split())) for i in f if i]

res = [10**6]*(k+1)
for i in range(1, len(res)):
    for r, m in arr:
        if m == i:
            res[i] = min(res[i], r-1)

ans = []
for i in range(1, len(res)-1):
    m1, m2 = res[i: i+2]
    if m1<m2:
        ans.append([m1, i])
    else:
        ans.append([m2, i])
ans = sorted(ans, key=lambda x: (-x[0], x[1]))
print(ans[0])
#21028 6660
def d(n):
    div = set()
    for i in range(2, round(n**.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

c = 0
res = []
for n in range(1200000, 0, -1):
    div = [i for i in d(n) if i<=n//2]
    s = sum(div[-3:]) if len(div)>=3 else 0
    if s!=n and s%2022==0 and s and c<5:
        res.append([n, s])
        c += 1
    if c==5: break
for i in sorted(res): print(*i)


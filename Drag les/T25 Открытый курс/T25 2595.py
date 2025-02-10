def d(n):
    div = set()
    for i in range(2, round(n**0.5)+1):
        if n%i==0: div |= {i, n//i}
    return sorted(div)

c = 0
for n in range(400_000_001, 400_010_000):
    div = d(n)
    p = 1
    if len(div)>=5:
        for i in div[:5]:
            p *= i
        last = div[4]
    if p%100==17 and p<=n and c<5:
        print(p, last)
        c += 1
# 782217 37
# 166617 33
# 2880117 93
# 74874717 111
# 725517 53
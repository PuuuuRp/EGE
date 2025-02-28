def d(n):
    div = set()
    for i in range(2, round(n**.5)+1):
        if n%i==0:
            div |= {i, n//i}
    if len(div)>=7: return sorted(div)
    return 0

c = 0
for n in range(400_000_001, 10**18):
    div = d(n)
    if div and c<5:
        c += 1
        print(div[-7], len(div))
    if c==5: break

# 34 10
# 2962963 14
# 1793722 30
# 21052632 62
# 754717 14
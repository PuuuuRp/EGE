def d(n):
    div = set()
    for i in range(2, round(n**.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

c = 0
for n in range(400*10**6+1, 10**12):
    div = d(n)
    D = div[-7] if len(div)>=7 else 0
    if D:
        c += 1
        print(D, len(div))
    if c==5: break

# 34 10
# 2962963 14
# 1793722 30
# 21052632 62
# 754717 14
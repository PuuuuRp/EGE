def d(n):
    div = set()
    for i in range(2, round(n**0.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

c = 0
for n in range(700001, 10**8):
    div = d(n)
    m = min(div) + max(div) if div else 0
    if m%10==4 and c<5:
        c += 1
        print(n, m)
    if c==5: break

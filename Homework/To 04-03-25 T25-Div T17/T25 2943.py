def d(n):
    div = set()
    for i in range(2, round(n**0.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

c = 0
for n in range(220001, 10**12):
    div = d(n)
    m = max(div)+min(div) if div else 0
    if m%10==4 and c<5:
        c += 1
        print(n, m)
    if c==5: break

# 220004 110004
# 220023 73344
# 220024 110014
# 220033 20014
# 220043 1044
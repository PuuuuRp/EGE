def d(n):
    div = set()
    for i in range(2, round(n**.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

c = 0
for n in range(300_001, 10**12):
    div = d(n)
    m = max(div)-min(div) if div else 0
    if m%10==6:
        c += 1
        print(n, m)
    if c==5: break

# 300005 59996
# 300016 150006
# 300027 100006
# 300031 1326
# 300036 150016
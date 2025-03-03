def d(n):
    div = set()
    for i in range(2, round(n**0.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return div

def pr(n): return n>1 and not d(n)

c = 0
for n in range(1_273_548, 10**12):
    m = 0 if pr(n) else sum(d(n))
    if pr(m%100_000) and c<5:
        print(n, m)
        c += 1
    if c==5: break

# 1273566 1637537
# 1273570 1139869
# 1273578 1287317
# 1273582 651769
# 1273590 2225609
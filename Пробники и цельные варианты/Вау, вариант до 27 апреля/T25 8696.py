def d(n):
    div = set()
    for i in range(2, round(n**.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

def pr(n):
    return n>1 and not d(n)

c = 0
for n in range(1273548, 10**12):
    div = d(n)
    m = sum(div)
    if pr(m%100000):
        c += 1
        print(n, m)
    if c==5: break

# 1273566 1637537
# 1273570 1139869
# 1273578 1287317
# 1273582 651769
# 1273590 2225609
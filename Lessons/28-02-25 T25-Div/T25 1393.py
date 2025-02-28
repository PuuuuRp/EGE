def d(n):
    div = set()
    for i in range(2, round(n**.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

def pr(n): return n>1 and not d(n)

c = 0
for n in range(650001, 10**12):
    div = d(n)
    p = [i for i in div if pr(i)]
    F = sum(p)//len(p) if p else 0
    if F%37==23 and c<4:
        c += 1
        print(n, F)
    if c==4: break

# 650090 60
# 650153 282
# 650155 3945
# 650208 134
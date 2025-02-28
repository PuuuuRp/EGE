def d(n):
    div = set()
    for i in range(2, round(n**.5)+1):
        if n%i==0:
            div |= {i, n//i, n}
    return sorted(div)

c = 0
N = 750_000
for k in range(1, 10**10):
    n = k+N
    div = d(n)
    div_2 = [i for i in div if i%2==0] if div else []
    if len(div_2)%2!=0 and c<5:
        print(k, len(div_2))
        c += 1
    if c==5: break

# 1538 3
# 3992 9
# 6450 27
# 8912 63
# 11378 3
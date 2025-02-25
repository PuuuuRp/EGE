def d(n):
    div = set()
    for i in range(2, round(n**0.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

c = 0
for n in range(700001, 10**8):
    div = d(n)
    d_7 = [i for i in div if i%10==7 and i!=7]
    if d_7 and c<5:
        c += 1
        print(n, min(d_7))
    if c==5: break

# 700002 27
# 700003 37
# 700005 6087
# 700007 77
# 700008 29167
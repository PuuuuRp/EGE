def d(n):
    div = set()
    for i in range(2, round(n**0.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

c = 0
for n in range(800001, 10**8):
    div = d(n)
    div = [i for i in div if i%10==9 and i!=9]
    if  div and c<5:
        c += 1
        print(n, min(div))
    if c==5: break

# 800004 818
# 800006 538
# 800008 88
# 800010 18
# 800014 38
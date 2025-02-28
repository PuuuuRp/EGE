def d(n):
    div = set()
    for i in range(2, round(n**0.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

c = 0
res = []
for n in range(699999, 0, -1):
    div = d(n)
    m = sum(div)//len(div) if div else 0
    if m%1000==313 and c<7:
        c += 1
        print(n, m)
    if c==7: break

# 698196 43313
# 697664 31313
# 696525 22313
# 695940 33313
# 695606 31313
# 695533 18313
# 695526 28313
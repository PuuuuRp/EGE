def d(n):
    div = set()
    for i in range(2, round(n**.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return div

cnt = 0
for n in range(700000-1, 0, -1):
    div = d(n)
    M = sum(div)//len(div) if div else 0
    if M%1000==313:
        cnt += 1
        print(n, M)
        if cnt == 7: break

# 698196 43313
# 697664 31313
# 696525 22313
# 695940 33313
# 695606 31313
# 695533 18313
# 695526 28313
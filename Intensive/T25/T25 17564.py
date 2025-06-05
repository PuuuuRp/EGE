def d(n):
    div = set()
    for i in range(2, round(n**.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

cnt = 0
for n in range(700001, 10**12):
    div = d(n)
    M = min(div) + max(div) if div else 0
    if M%10==4:
        cnt += 1
        print(n, M)
        if cnt==5: break

# 700004 350004
# 700009 41194
# 700023 233344
# 700024 350014
# 700044 350024
def d(n):
    div = set()
    for i in range(2, round(n**0.5)+1):
        if n%i==0:
            div |= {i,n//i}
    return sorted(div)

c = 0
for n in range(800001, 10**8):
    div = d(n)
    M = min(div) + max(div) if div else 0
    if M%10==4 and c<5:
        c += 1
        print(n, M)
    if c==5: break

# 800004 400004
# 800009 114294
# 800013 266674
# 800024 400014
# 800033 61554
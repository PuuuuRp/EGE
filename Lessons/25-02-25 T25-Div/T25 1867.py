def d(n):
    div = set()
    for i in range(2, round(n**0.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

c = 0
for n in range(500001, 10**8):
    div = d(n)
    div = [i for i in div if i%10==8 and i != 8]
    if div and c<5:
        c += 1
        print(n, min(div))
    if c==5: break

# 500002 178
# 500004 18
# 500016 48
# 500018 58
# 500020 4348
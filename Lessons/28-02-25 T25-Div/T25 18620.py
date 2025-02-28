def d(n):
    div = set()
    for i in range(2, round(n**0.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

for n in range(112500000, 112550001):
    div = d(n)
    m = sum(div[-2:]) if len(div)>=2 else 0
    if m%10000==1214:
        print(n)

# 112508413
# 112520369
# 112523549
# 112534952
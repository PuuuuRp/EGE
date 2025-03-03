def d(n):
    div = set()
    for i in range(2, round(n**.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted([i for i in div if i%2!=0])

c = 0
for n in range(200_000_001, 10**12):
    D = d(n)[-6] if len(d(n))>5 else 0
    if D and c<5:
        print(n, D)
        c += 1
    if c==5: break

# 200000003 48391
# 200000004 42123
# 200000005 5
# 200000008 5101
# 200000009 113443
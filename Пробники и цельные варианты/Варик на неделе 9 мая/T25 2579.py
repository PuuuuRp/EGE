def d(n):
    div = set()
    for i in range(2, round(n**.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

cnt = 0
for n in range(10**7+1, 10**12):
    div = d(n)
    S = sum(div[-3:]) if len(div)>=3 else 0
    if any(S**.5 == i for i in range(2, 10**4)):
        print(S)
        cnt += 1
        if cnt ==5: break


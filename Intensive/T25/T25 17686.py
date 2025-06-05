def d(n):
    div = set()
    for i in range(2, round(n**.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sorted(div)

cnt = 0
for n in range(700001, 10**12):
    div = [i for i in d(n) if i!=7 and i%10==7]
    if div:
        cnt += 1
        print(n, min(div))
        if cnt==5:
            break

# 700002 27
# 700003 37
# 700005 6087
# 700007 77
# 700008 29167
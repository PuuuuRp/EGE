def d(n):
    arr = set()
    for i in range(2, round(n**.5)+1):
        if n%i==0:
            arr |= {i, n//i}
    return sorted(arr)

cnt = 0
for n in range(500001, 10**12):
    div = d(n)
    R = sum(div) if div else 0
    if R>0 and R%10==9:
        cnt += 1
        print(n, R)
        if cnt==5: break

# 500014 250009
# 500038 495289
# 500040 1170359
# 500054 250029
# 500058 667289
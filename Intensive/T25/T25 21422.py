def d(n):
    arr = set()
    for i in range(2, round(n**.5)+1):
        if n%i==0:
            arr |= {i, n//i}
    return sorted(arr)

cnt = 0
for n in range(1125001, 10**12):
    div = [i for i in d(n) if i!=7 and i%10==7]
    if div:
        cnt += 1
        print(n, min(div))
        if cnt==5: break

# 1125003 467
# 1125006 97
# 1125009 17
# 1125011 3187
# 1125012 177
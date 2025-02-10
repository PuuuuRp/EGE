def d(n):
    div = set()
    for i in range(2, round(n**0.5)+1):
        if n%i==0: div |= {i, n//i}
    return sorted(div)

for n in range(1204300, 1204381):
    div = [i for i in d(n) if i%2==0]
    s = sum(div)
    if s!=0 and s%10==0:
        print(n, s)
# 1204328 948760
# 1204354 27530
# 1204356 1204380
# 1204360 1324880
# 1204366 4850
# 1204370 291070
# 1204378 172070
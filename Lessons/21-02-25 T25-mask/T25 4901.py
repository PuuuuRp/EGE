from fnmatch import *

def d(n):
    div = set()
    for i in range(1, round(n**0.5)+1):
        if n%i==0:
            div |= {i, n//i}
    return sum(i for i in div)

c = 0
res = []
for i in range(16606, 10**9):
    if fnmatch(str(i), '?6*6*?6') and c<7\
            and i%6==0 and i%7==0 and i%8==0:
        c += 1
        res.append([i, d(i)])
    if c==7: break
for i in sorted(res): print(*i)


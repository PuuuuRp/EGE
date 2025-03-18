from functools import *
@lru_cache(None)
def f(n):
    if n>7000: return n+4
    return 3*n+5+f(n+3)
for n in range(7001, 706, -1):
    f(n)
print(f(707)-f(716))
#6405
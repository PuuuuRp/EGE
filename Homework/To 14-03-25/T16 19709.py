from functools import *
@lru_cache(None)
def f(n):
    if n==1: return 1
    if n>1: return n**3 + f(n-1)
    return 0
for n in range(2026):
    f(n)
print(f(2025)-f(2022))
#24874421616
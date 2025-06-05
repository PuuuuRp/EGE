from functools import *
@lru_cache(None)
def f(n):
    if n==1: return 1
    return n*f(n-1)

for n in range(1, 2025): f(n)

print((f(2024)*2 + f(2023))//f(2022))
#8191127
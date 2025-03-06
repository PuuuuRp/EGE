from functools import *
@lru_cache(None)
def f(n):
    if n<110: return n
    return n+f(n-1)
for n in range(100, 2026):
    f(n)
print(f(2025)-f(2021))
#8094
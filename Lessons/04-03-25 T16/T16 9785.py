from functools import *
@lru_cache(None)
def f(n):
    if n<7: return 7
    return n+1+f(n-2)
for n in range(2025):
    f(n)
print(f(2024)-f(2020))
#4048
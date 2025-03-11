from functools import *
@lru_cache(None)
def f(a, n):
    if a==n: return 1
    if a<n: return 0
    return f(a-1, n)+f(a//2, n)
print(f(30, 12)*f(12, 1))
#376
from functools import *
@lru_cache(None)
def f(a, n):
    if a==n: return 1
    if a<n: return 0
    return f(a-2, n)+f(a//2, n)
print(f(32, 14)*f(14,1))
#54
from functools import *
@lru_cache(None)
def f(a, n):
    if a==n: return 1
    if a<n or a==7: return 0
    return f(a-1, n)+f(a-3, n)+f(a//2, n)
print(f(19, 10)*f(10, 3))
#133
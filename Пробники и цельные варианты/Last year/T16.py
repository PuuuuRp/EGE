from functools import *
@lru_cache(None)
def f(n):
    if n<=6: return 1
    return 2*n+3+f(n-1)
for n in range(6, 6189): f(n)

print(f(6188)-f(6185))
#37131
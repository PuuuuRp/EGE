from functools import *
@lru_cache(None)
def f(a, n):
    if a==n: return 1
    if a==12 or a>n: return 0
    return f(a+1, n)+f(a+2, n)+f(a*3, n)
print(f(2, 9)*f(9, 19))
#650
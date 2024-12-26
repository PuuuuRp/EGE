from functools import *
@lru_cache(None)
def f(n, a):
    if n == a: return 1
    if n < a or n == 24: return 0
    return f(n-1, a)+f(n-6, a)+f(n//2, a)

print(f(34, 29)*f(29, 19)*f(19, 6))
#115
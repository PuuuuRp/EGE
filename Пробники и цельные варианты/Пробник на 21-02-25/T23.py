from functools import *
@lru_cache(None)
def f(x, a):
    if x==a: return 1
    if x<a or x==36 or x==100: return 0
    return f(x//2, a)+f(x//3, a)+f(x-3, a)

print(f(163, 45)*f(45, 3))
#690
from functools import *
@lru_cache(None)
def f(n):
    if n<3: return 3
    return 2*n+5+f(n-2)
for n in range(3028):
    f(n)
print(f(3027)-f(3023))
#12114
from functools import *
@lru_cache(None)
def f(n):
    if n<11: return n
    if n%2==0: return 2*n - 3 + f(n-2)
    return 3*n-4+f(n-3)
for n in range(11, 5501):
    f(n)
print(f(5500)-f(5497))
#16492
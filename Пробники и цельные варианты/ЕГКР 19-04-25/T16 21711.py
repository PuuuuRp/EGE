from functools import *
@lru_cache(None)
def f(n):
    if n<20: return n
    return (n - 6) * f(n - 7)

for n in range(20, 47872): f(n)

print((f(47872) - 290*f(47865))//f(47858))
#2276939784
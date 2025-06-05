from functools import *
@lru_cache(None)
def f(n):
    if n<=5: return 1
    return n+f(n-2)

for n in range(5, 2127): f(n)

print(f(2126)-f(2122))
#4250
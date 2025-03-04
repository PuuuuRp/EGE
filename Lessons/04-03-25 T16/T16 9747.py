from functools import *
@lru_cache(None)
def f(n):
    if n<11: return n
    return n+f(n-1)
for n in range(0, 2024):
    f(n)
print(f(2024)-f(2021))
#6069
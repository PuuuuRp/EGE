from functools import *
@lru_cache(None)
def f(n):
    if n>3000: return 1
    if n%2==0: return f(n+1)-n+1
    return f(n+2)-n*2+2

for n in range(3001, 30, -1): f(n)

print(2*f(39) - 2*f(34))
#346
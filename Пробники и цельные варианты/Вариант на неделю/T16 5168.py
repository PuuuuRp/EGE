from functools import *
@lru_cache(None)
def f(n):
    if n >= 10000: return n
    if n%2==0: return f(n+1)+n**2-3*(n-1)
    return f(n+2)+5*n-n+1
for n in range(10000, 89, -1):
    f(n)
print(f(90)-f(99))
#9341
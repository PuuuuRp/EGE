from functools import *
@lru_cache(None)
def f(n):
    if n<100: return n**2
    if n%2==0: return f(n-1)//2
    return 2*f(n-1)
for n in range(16385):
    f(n)
print(1000*f(16384)//f(7777))
#500
from functools import *
@lru_cache(None)
def f(n):
    if n<=3: return n
    return (n-2)*f(n-2)
for n in range(3, 2021):
    f(n)
print((f(1024) + 2*f(1022)-2*f(1021)) // f(1020))
#1044403
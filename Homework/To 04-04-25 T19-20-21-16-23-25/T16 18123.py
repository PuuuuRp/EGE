from functools import *
@lru_cache(None)
def f(n):
    if n>=2010: return n
    return f(n+3)+f(n+2)+f(n+1)
for n in range(2000, 2011):
    f(n)
print((f(2000)-2*(f(2002)+f(2003)))//f(2004))
#1
from functools import *
def num(a):
    a = [int(i) for i in str(a)]
    return max(a)

@lru_cache(None)
def f(a, b):
    if a==b: return 1
    if a<b: return f(a+2, b) + f(a+num(a), b)
    return 0

print(f(32,55)*f(55, 76))
#476
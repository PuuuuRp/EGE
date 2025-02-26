from functools import *
@lru_cache(None)
def f(x):
    if x==38: return 1
    if x==22 or x>38: return 0
    return f(x+3)+f(x+4)
print(f(16))
#16
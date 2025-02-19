from functools import *
@lru_cache(None)
def f(n):
    if n<5: return 4
    if n>4: return 4*f(n-4)

for n in range(4, 4445):
    f(n)
print(f(4444)/f(4400))
#4194304
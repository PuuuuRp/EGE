from functools import *
@lru_cache(None)
def f(n):
    if n==1: return 1
    if n>1: return (n+1)*f(n-1)
    return 0
for n in range(2025):
    f(n)
print((f(2024)-3*f(2023))//f(2022))
#4092528
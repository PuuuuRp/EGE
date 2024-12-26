from functools import *

def h(p):
    n = p
    return n+3, n+6, n*3

@lru_cache(None)
def f(p):
    n = p
    if n > 131: return 'L0'
    if any(f(i)=='L0' for i in h(p)): return 'W1'
    if all(f(i)=='W1' for i in h(p)): return 'L2'
    if any(f(i)=='L2' for i in h(p)): return 'W3'
    if all(f(i) in ['W1', 'W3'] for i in h(p)): return 'L4'

for p in range(132, 0, -1):
    print(p, f(p))
#19: 41
#20: 14 35
#21: 32
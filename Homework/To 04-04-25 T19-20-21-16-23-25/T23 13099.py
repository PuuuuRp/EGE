from sys import *
setrecursionlimit(10**6)
def f(a, n, c):
    if a==n: return 1
    if a>20 or c==2: return 0
    return f(a-1, n, c+1)+f(a*2, n, 0)+f(a*3, n, 0)
print(f(3, 15, 0))
#6
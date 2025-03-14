from sys import *
setrecursionlimit(10**7)

def prime(n):
    for i in range(n+1, 4000):
        for x in range(2, round(i**.5)+1):
            if i%x==0: break
        return i

def t(n):
    for i in [4, 8, 16, 32, 64, 128, 512, 1024, 2048, 4096]:
        if i>n: return i

def f(a, n):
    if a==n: return 1
    if a>n or a==3 or a==14: return 0
    b = int(prime(a))
    c = t(a)
    if a%10!=0:
        return f(a+b, n)+f(a+c, n)+f(a + a%10, n)
    else: return f(a+b, n)+f(a+c, n)
print(f(2, 1024)*f(1024, 3072))
#
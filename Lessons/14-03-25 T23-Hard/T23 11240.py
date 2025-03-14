def f(a, n, c=0):
    if a==n: return 1
    if a>n: return 0
    if c==1: return f(a+2, n)+f(a*3, n)
    return f(a+2, n)+f(a*3, n)+f(a**2, n, 1)
print(f(2, 64))
#55
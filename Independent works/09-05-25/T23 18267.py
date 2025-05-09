def f(a, n, c):
    if a==n and c==0: return 1
    if a>n: return 0
    return f(a+2, n, 0)+f(a+5, n, 0)+f(a**2, n, 1)
print(f(4, 36, 0))
#319
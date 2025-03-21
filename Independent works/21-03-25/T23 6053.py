def f(a, n):
    if a==n: return 1
    if a>n or a==9: return 0
    return f(a+1, n) + f(a*2, n)
print(f(2, 12)*f(12, 42))
#55
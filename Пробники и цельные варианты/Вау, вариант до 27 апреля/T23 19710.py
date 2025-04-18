def f(a, n):
    if a==n: return 1
    if a>n or a==8: return 0
    return f(a+3, n)+f(a*2, n)
print(f(2, 32)*f(32, 76))
#21
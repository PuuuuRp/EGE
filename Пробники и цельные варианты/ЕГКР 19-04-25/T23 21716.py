def f(a, n):
    if a==n: return 1
    if a>n or a==56: return 0
    return f(a+3, n)+f(a+7, n)+f(a*3, n)
print(f(12, 40)*f(40, 72)*f(72, 89))
#324
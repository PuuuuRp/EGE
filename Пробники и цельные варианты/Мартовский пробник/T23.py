def f(a, n):
    if a==n: return 1
    if a==8 or a>n: return 0
    return f(a+1, n)+f(a*2, n)+f(a*5, n)
print(f(2, 27)*f(27, 54))
#64
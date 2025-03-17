def f(a,n):
    if a==n: return 1
    if a>n: return 0
    return f(a+2, n)+f(a*2, n)+f(a+5, n)
print((f(9, 23)+f(14, 23))*f(23, 35))
#44
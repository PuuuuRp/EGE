def f(a, n):
    if a==n: return 1
    if a>n: return 0
    return f(a+1, n)+f(a+2, n)+f(a*2, n)
print(f(4, 11)*f(11, 13)*f(13, 15))
#100
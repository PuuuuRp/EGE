def f(a, n):
    if a==n: return 1
    if a>n or a==35: return 0
    return f(a+1, n)+f(a+2, n)+f(a*2, n)

print(f(7, 13)*f(13, 15)*f(15, 51))
#174034068
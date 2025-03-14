def f(a, n, c):
    if a==n and c==51: return 1
    if a>n: return 0
    return f(a*4, n, c+1)+f(a+1, n, c+1)+f(a*3, n, c+1)
print(f(2, 404, 0))
#319
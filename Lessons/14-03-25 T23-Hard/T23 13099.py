def f(a, n, c=0):
    if a==n: return 1
    if a>n+1: return 0
    if c==0:
        return f(a * 2, n, c) + f(a * 3, n, c) + f(a - 1, n, 1)
    return f(a*2, n)+f(a*3, n)
print(f(3, 15))
#6
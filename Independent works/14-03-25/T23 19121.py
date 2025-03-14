def f(a, n):
    if a==n: return 1
    if a<n: return 0
    return f(a-3, n)+f(a//3, n)
print(f(35, 8)*f(8, 1))
#3
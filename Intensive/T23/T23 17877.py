def f(a, n):
    if a==n: return 1
    if a<n: return 0
    return f(a-2, n)+f(a//2, n)

print(f(38, 16)*f(16, 2))
#36
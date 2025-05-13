def f(a, n):
    if a==n: return 1
    if a<n or a==20: return 0
    return f(a-2, n)+f(a-3, n)+f(a//5, n)
print(f(41, 10)*f(10, 5))
#2912
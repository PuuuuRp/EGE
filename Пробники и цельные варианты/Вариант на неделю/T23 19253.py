def f(a, n):
    if a==n: return 1
    if a==24 or a<n: return 0
    return f(a-1, n)+f(a-6, n)+f(a//2, n)
print(f(34, 29)*f(29, 19)*f(19, 6))
#115
def f(a, n):
    if a==n: return 1
    if a<n or a==15: return 0
    return f(a-2, n)+f(a-3, n)+f(a//3, n)

print(f(48, 25)*f(25, 17)*f(17, 4))
#9540
def f(a, n, c):
    if a==n and c<=15: return 1
    if a>n or c>15: return 0
    if a%2==0:
        return f(a+2, n, c+1)+f(a+3, n, c+1)+f(a*2+1, n, c+1)
    return f(a+2, n, c)+f(a+3, n, c)+f(a*2+1, n, c)
print(f(1, 55, 0))
#4197234
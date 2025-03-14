def f(a, n, c=0):
    if a==n and c==x: return 1
    if a>n: return 0
    if any(i**2 == a for i in range(0, 10)):
        return f(a-1, n, c+1)
    return f(a+2, n, c)+f(a+3, n, c)+f(a*3, n, c)

res = []
for x in range(1, 10):
    res.append(f(5, 50))
print(max(res))
#130771
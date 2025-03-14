def f(a, n, c1, c2, c3):
    if a==n and c1<=4 and c2>=2 and c3==5: return 1
    if a>n: return 0
    return f(a*5, n, c1+1, c2, c3)+f(a*3, n, c1, c2+1, c3)+f(a+45, n, c1, c2, c3+1)
print(f(1, 2970, 0, 0, 0))
#74
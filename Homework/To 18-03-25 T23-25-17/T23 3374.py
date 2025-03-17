def f(a, n):
    if a==n: return 1
    if a<-50 or a>50: return 0
    return f(a+2, n)+f(a-3, n)
print(f(1, 30)) 
#
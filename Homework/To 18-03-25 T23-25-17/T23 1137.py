def f(a, n):
    if int(a, 2)==n: return 1
    if int(a,2)>n: return 0
    return f(bin(int(a, 2)+1)[2:], n)+f(a+'0', n)+f(a+'1', n)
print(f('100', 29))
#79
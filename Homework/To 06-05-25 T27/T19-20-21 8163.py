def f(x, s):
    if x>=348: return s%2==0
    if s==0: return 0
    h = [f(x+2, s-1), f(x+4, s-1), f(x*3, s-1)]
    return all(h) if s%2==0 else any(h)

def f1(x, s):
    if x>=348: return s%2==0
    if s==0: return 0
    h = [f1(x+2, s-1), f1(x+4, s-1), f1(x*3, s-1)]
    return any(h) if s%2==0 else any(h)

print([i for i in range(1, 348) if f1(i, 2)])
print([i for i in range(1, 348) if f(i, 3) and not f(i, 1)])
print([i for i in range(1, 348) if f(i, 4) and not f(i, 2)])
#39
#38 110
#108
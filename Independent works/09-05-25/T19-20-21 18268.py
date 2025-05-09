def f(x, y, s):
    if x+y<=72: return s%2==0
    if s==0: return 0
    h = [f(x-3, y, s-1), f(x//2 if x%2==0 else x//2+1, y, s-1), f(x, y-3, s-1), f(x, y//2 if y%2==0 else y//2+1, s-1)]
    return all(h) if s%2==0 else any(h)

def f1(x, y, s):
    if x+y<=72: return s%2==0
    if s==0: return 0
    h = [f(x-3, y, s-1), f(x//2 if x%2==0 else x//2+1, y, s-1), f(x, y-3, s-1), f(x, y//2 if y%2==0 else y//2+1, s-1)]
    return any(h) if s%2==0 else any(h)

print([i for i in range(23, 500) if f1(50, i, 2)])
print([i for i in range(23, 500) if f(50, i, 3) and not f(50, i, 1)])
print([i for i in range(23, 500) if f(50, i, 4) and not f(50, i, 2)])
#94
#51 100
#103
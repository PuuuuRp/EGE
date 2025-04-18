def f(x, y, s):
    if x+y<=100: return s%2==0
    if s==0: return 0
    h = [f(x-3, y-3, s-1), f(x//2, y, s-1), f(x, y//2, s-1)]
    return all(h) if s%2==0 else any(h)

def f1(x, y, s):
    if x+y<=100: return s%2==0
    if s==0: return 0
    h = [f(x-3, y-3, s-1), f(x//2, y, s-1), f(x, y//2, s-1)]
    return any(h) if s%2==0 else any(h)

print([i for i in range(53, 400) if f1(48, i, 2)])
print([i for i in range(53, 400) if f(48, i, 3) and not f(48, i, 1)])
print([i for i in range(53, 400) if f(48, i, 4) and not f(48, i, 2)])
#59
#115 229
#124
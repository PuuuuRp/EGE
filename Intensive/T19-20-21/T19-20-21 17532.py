def f(x, y, s):
    if x+y>=65: return s%2==0
    if s==0: return 0
    h = [f(x+1, y, s-1), f(x*3, y, s-1), f(x, y+1, s-1), f(x, y*3, s-1)]
    return all(h) if s%2==0 else any(h)

def f1(x, y, s):
    if x+y>=65: return s%2==0
    if s==0: return 0
    h = [f(x+1, y, s-1), f(x*3, y, s-1), f(x, y+1, s-1), f(x, y*3, s-1)]
    return any(h) if s%2==0 else any(h)

print(*[i for i in range(1, 58) if f1(i, 6, 2)])
print(*[i for i in range(1, 58) if f(i, 6, 3) and not f(i, 6, 1)])
print(*[i for i in range(1, 58) if f(i, 6, 4) and not f(i, 6, 2)])
#7
#10 19
#18
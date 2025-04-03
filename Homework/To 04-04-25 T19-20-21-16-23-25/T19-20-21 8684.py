def f(x, y, s):
    if x+y>=175: return s%2==0
    if s==0: return 0
    h = [f(x+1, y, s-1), f(x*3, y, s-1), f(x, y+1, s-1), f(x, y*3, s-1)]
    return all(h) if s%2==0 else any(h)
def f1(x, y, s):
    if x+y>=175: return s%2==0
    if s==0: return 0
    h = [f(x+1, y, s-1), f(x*3, y, s-1), f(x, y+1, s-1), f(x, y*3, s-1)]
    return any(h) if s%2==0 else any(h)
print([s for s in range(1, 155) if f1(s, 19, 2)])
print([s for s in range(1, 155) if f(s, 19, 3) and not f(s, 19, 1)])
print([s for s in range(1, 155) if f(s, 19, 4) and not f(s, 19, 2)])
#4
#3
#51
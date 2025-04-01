def f(x, y, s):
    if x+y>=44: return s%2==0
    if s==0: return 0
    h = [f(x+y, y, s-1), f(x, x+y, s-1)]
    return all(h) if s%2==0 else any(h)
print([s for s in range(43) if f(11, s, 1)])
print([s for s in range(43) if f(11, s, 2)])
print([s for s in range(43) if f(s, s, 3) and not f(s, s, 1)])
#17
#8
#7 7
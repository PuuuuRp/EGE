def f(x, y, s):
    if x+y>=65: return s%2==0
    if s==0: return 0
    h = [f(x+1, y, s-1), f(x*3, y, s-1), f(x, y+1, s-1), f(x, y*3, s-1)]
    return all(h) if s%2==0 else any(h)
print([s for s in range(1, 59) if f(s, 6, 2)])
print([s for s in range(1, 59) if f(s, 6, 3) and not f(s, 6, 1)])
print([s for s in range(1, 59) if f(s, 6, 4) and not f(s, 6, 2)])
#7
#10 19
#18
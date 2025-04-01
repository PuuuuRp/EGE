def f(x, s):
    if x>=39: return s%2==0
    if s==0: return 0
    h = [f(x+1, s-1), f(x+3, s-1), f(x*2, s-1)]
    return all(h) if s%2==0 else any(h)
print([s for s in range(1, 39) if f(s, 2)])
print([s for s in range(1, 39) if f(s, 3) and not f(s, 1)])
print([s for s in range(1, 39) if f(s, 4) and not f(s, 2)])
#19
#16 18
#15
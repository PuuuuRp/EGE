def f(x, s):
    if x>=39: return s%2==0
    if s==0: return 0
    h = [f(x+1, s-1), f(x+3, s-1), f(x*2, s-1)]
    return all(h) if s%2==0 else any(h)

print([i for i in range(1, 39) if f(i, 2)])
print([i for i in range(1, 39) if f(i, 3) and not f(i, 1)])
print([i for i in range(1, 39) if f(i, 4) and not f(i, 2)])
#19
#16 18
#15
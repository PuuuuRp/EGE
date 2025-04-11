def f(x, s, c=0):
    if x>40: return s%2==0
    if s==0: return 0
    if c==0: h = [f(x+3, s-1, 1), f(x+6, s-1, 2), f(x*2, s-1, 3)]
    elif c==1: h = [f(x+6, s-1, 2), f(x*2, s-1, 3)]
    elif c==2: h = [f(x+3, s-1, 1), f(x*2, s-1, 3)]
    elif c==3: h = [f(x+3, s-1, 1), f(x+6, s-1, 2)]
    return all(h) if s%2==0 else any(h)

print([i for i in range(2, 37) if f(i, 2)])
print([i for i in range(2, 37) if f(i, 3) and not f(i, 1)])
print([i for i in range(2, 37) if f(i, 4) and not f(i, 2)])
#20
#17
#6 8
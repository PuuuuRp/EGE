def f1(x, s):
    if x>665: return s%2==0
    if s==0: return False
    h = [f(x+3, s-1), f(x*3, s-1), f(x+x**2, s-1),]
    return any(h) if s%2==0 else any(h)
def f(x, s):
    if x>665: return s%2==0
    if s==0: return False
    h = [f(x+3, s-1), f(x*3, s-1), f(x+x**2, s-1),]
    return all(h) if s%2==0 else any(h)
print('19)', [s for s in range(666) if f1(s, 2)])
print('20)', [s for s in range(666) if f(s, 3) and not f(s, 1)])
print('21)', [s for s in range(666) if f(s, 4) and not f(s, 2)])
#5
#8 22
#19
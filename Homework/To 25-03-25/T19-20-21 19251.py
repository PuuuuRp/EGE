def f(x, s):
    if x>=132: return s%2==0
    if s==0: return False
    h = [f(x+3, s-1), f(x+6, s-1), f(x*3, s-1)]
    return all(h) if s%2==0 else any(h)
print('19)', [s for s in range(1, 132) if f(s, 2)])
print('20)', [s for s in range(1, 132) if not f(s, 1) and f(s, 3)])
print('21)', [s for s in range(1, 132) if not f(s, 2) and f(s, 4)])
#41
#14 35
#32
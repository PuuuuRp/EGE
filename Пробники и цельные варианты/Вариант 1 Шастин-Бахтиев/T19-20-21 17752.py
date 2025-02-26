def f(x, s):
    if x>=54: return s%2==0
    if s==0: return 0
    h = [f(x+2, s-1), f(x*2, s-1)]
    return all(h) if s%2==0 else any(h)

print('19)', [s for s in range(1, 54) if f(s, 2)])
print('20)', [s for s in range(1, 54) if f(s, 3) and not f(s, 1)])
print('21)', [s for s in range(1, 54) if not f(s, 2) and f(s, 4)])

#25
#13 23
#21
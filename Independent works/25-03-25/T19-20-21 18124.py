def f(x, s):
    if x<=33: return s%2==0
    if s==0: return False
    h = [f(x-3, s-1), f(x-5, s-1),
         f(x//3 if x%3==0 else x//3+1, s-1)]
    return any(h) if s%2==0 else any(h)
print('19)', sum(f(s, 2) for s in range(34, 500)))
print('20)', [s for s in range(34, 500) if f(s, 3) and not f(s, 1)])
print('21)', [s for s in range(34, 500) if f(s, 4) and not f(s, 2)])
#3
#103 306
#108
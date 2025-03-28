def f(x, s):
    if x>=67: return s%2==0
    if s==0: return False
    h = [f(x+1, s-1), f(x+3, s-1), f(x*2, s-1)]
    return all(h) if s%2==0 else any(h)

print('19)', [i for i in range(1, 67) if f(i, 2)])
print('20)', [i for i in range(1, 67) if f(i, 3) and not f(i, 1)])
print('21)', [i for i in range(1, 67) if f(i, 4) and not f(i, 2)])
#
#
#
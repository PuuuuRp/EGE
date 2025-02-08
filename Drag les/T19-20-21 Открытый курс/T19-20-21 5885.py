def f(m, s):
    if m==42: return s%2==0
    if s==0: return False
    if m<42: h = [f(m+1, s-1), f(m+3, s-1), f(m+7, s-1)]
    if m>42: h = [f(m - 1, s - 1), f(m - 3, s - 1), f(m - 7, s - 1)]
    return any(h) if (s+1)%2==0 else all(h)

print('19)', [s for s in range(0, 100) if f(s, 2)])
print('20)', [s for s in range(0, 100) if f(s, 3) and not f(s, 1)])
print('21)', [s for s in range(0, 100) if f(s, 4) and not f(s, 2)])
#28
#31 37
#50
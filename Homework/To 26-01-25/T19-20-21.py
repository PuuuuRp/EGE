def f(m, n, s):
    if m+n>=300: return s%2==0
    if s==0: return False
    h = [f(m+3, n, s-1), f(m, n+2, s-1), f(m*2, n, s-1), f(m, n*2, s-1)]
    return any(h) if (s+1)%2==0 else all(h)

print('19)', [s for s in range(1, 300) if f(20, s, 2)])
print('20)', [s for s in range(1, 300) if f(20, s, 3) and not f(20, s, 1)])
print('21)', [s for s in range(1, 300) if f(20, s, 5) and not f(20, s, 3)])
#139
#129 138
#68
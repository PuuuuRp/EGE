def f(x, y, s):
    if x*y>=777: return s%2==0
    if s==0: return False
    h = [f(x+3, y, s-1), f(x*2, y, s-1), f(x, y+3, s-1), f(x, y*2, s-1)]
    #return all(h) if s%2==0 else all(h)
    return all(h) if s%2==0 else any(h)

print('19)', [s for s in range(1, 111) if f(7, s, 2)])
print('19)', [s for s in range(1, 111) if f(7, s, 3) and not f(7, s, 1)])
print('19)', [s for s in range(1, 111) if f(7, s, 4) and not f(7, s, 2)])

#53
#25 52
#33
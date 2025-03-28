def f(x, y, s):
    if x+y>=77: return s%2==0
    if s==0: return False
    h = [f(x+3, y, s-1), f(x*3, y, s-1), f(x, y+3, s-1), f(x, y*3, s-1)]
    return all(h) if s%2==0 else any(h)
print('19)', [i for i in range(1, 65) if f(12, i, 2)])
print('20)', [i for i in range(1, 65) if f(12, i, 3) and not f(12, i, 1)])
print('21)', [i for i in range(1, 65) if f(12, i, 4) and not f(12, i, 2)])
#21
#7 18
#2
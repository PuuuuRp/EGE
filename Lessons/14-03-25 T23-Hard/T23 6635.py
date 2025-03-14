def f(a, c):
    if c==13 and a<0: return [a]
    if c>13: return []
    return f(a-3, c+1)+f(a*(-3), c+1)
print(len(set(f(333, 0))))
#2224
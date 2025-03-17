def f(a, c, sh):
    if not sh: return [a]
    if sh<0: return []
    if c==1: return f(a+7, 2, sh-1)+f(a*4,3, sh-1)
    if c==2: return f(a+1, 1, sh-1)+f(a*4, 3, sh-1)
    if c==3: return f(a+7, 2, sh-1)+f(a+1, 1, sh-1)
    return f(a + 7, 2, sh - 1) + f(a + 1, 1, sh - 1)+f(a*4,3, sh-1)
print(len(set(f(1, 0, 24))))
#1091793
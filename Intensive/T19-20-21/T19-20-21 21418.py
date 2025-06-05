def f(x, s):
    if x<=87: return s%2==0
    if s==0: return 0
    h = [f(x-2, s-1), f(x//2, s-1)]
    return all(h) if s%2==0 else any(h)

print(*[i for i in range(89, 500) if f(i, 2)])
print(*[i for i in range(89, 500) if f(i, 3) and not f(i, 1)])
print(*[i for i in range(89, 500) if f(i, 4) and not f(i, 2)])
#176
#178 179
#180
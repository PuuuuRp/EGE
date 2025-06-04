def f(a, q):
    res = ''
    while a:
        res += str(a%q)
        a //= q
    return res[::-1]

m = 10**18
for n in range(1, 10000):
    r = f(n, 3)
    if n%3==0: r += r[-2:]
    else: r += f(n%3*5, 3)
    if int(r, 3) > 133: m = min(m, int(r, 3))
print(m)
#141
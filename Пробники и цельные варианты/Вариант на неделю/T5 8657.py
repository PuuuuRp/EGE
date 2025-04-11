def toq(a, q):
    res = ''
    while a:
        res += str(a%q)
        a //= q
    return res[::-1]

res = []
for n in range(1, 10000):
    r = toq(n, 3)
    if n%5==0: r += r[-3:]
    else: r += toq(n%5*5, 3)
    r = int(r, 3)
    if r < 5496: res.append(n)
print(max(res))
#606
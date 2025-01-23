def toq(a, q):
    res = ''
    while a:
        res += str(a%q)
        a //= q
    return res[::-1]

res = []
for n in range(1, 1000):
    r = toq(n, 3)
    if n%3==0: r += r[-2:]
    else: r += toq(n%3*5, 3)
    if int(r, 3) > 133:
        res.append(int(r, 3))
print(min(res))
#141
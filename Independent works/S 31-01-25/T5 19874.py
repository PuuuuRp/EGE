def toq(a, q):
    res = ''
    while a:
        res += str(a%q)
        a //= q
    return res[::-1]
res = []
for n in range(10, 10000):
    r = toq(n,3)
    if n%4 == 0: r += r[-3:]
    else: r = '1'+r+'20'
    if int(r, 3) > 423:
        res.append(int(r, 3))
print(min(res))
#438
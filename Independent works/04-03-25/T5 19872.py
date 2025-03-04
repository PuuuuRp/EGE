def toq(a, q):
    res = ''
    while a:
        res += str(a%q)
        a //= q
    return res[::-1]

res = []
for n in range(1, 1000):
    r = toq(n, 7)
    if n%2==0: r = '52' + r + '1'
    else: r = r[-1] + r[1:-1] + r[0] + '15'
    r = toq(int(r, 7), 7)
    if len(r)==4:
        res.append(n)
print(res[-1])
#721
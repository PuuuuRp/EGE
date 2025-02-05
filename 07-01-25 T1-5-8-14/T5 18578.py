def toq(a, q):
    res = ''
    while a:
        res += str(a%q)
        a //= q
    return res[::-1]

res = []
for n in range(1, 10000):
    r = toq(n, 4)
    if n%4 == 0:
        r = '2'+r+'03'
    else:
        r += toq(n%4*5, 4)
    if int(r, 4) <= 567:
        res.append(n)
print(res[-1])
#34
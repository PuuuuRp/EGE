def toq(a, q):
    al = '0123456789ab'
    res = ''
    while a:
        res += al[a%q]
        a //= q
    return res[::-1]

res = []
for n in range(1, 1000):
    r = toq(n, 12)
    if n%3 == 0: r = '1'+r+'b'
    else: r = '2'+r+'0'
    r = int(r, 12)
    if r < 1996: res.append(r)
print(max(res))
#1994
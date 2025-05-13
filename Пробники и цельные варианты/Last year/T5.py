def toq(a, q):
    res = ''
    while a:
        res += str(a%q)
        a //= q
    return res[::-1]

res = []
for n in range(1, 100000):
    r = toq(n, 7)
    if r.count('2')%2==0: r += '555'
    else: r = '1' + r
    r = int(r, 7)
    if r < 3799:
        res.append(n)
print(max(res))
#1395
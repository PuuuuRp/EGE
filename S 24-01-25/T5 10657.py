def toq(a, q):
    res = ''
    while a:
        res += str(a%q)
        a //= q
    return res[::-1]

res = []
for n in range(1, 1000):
    r = toq(n, 3)
    pl = sum(int(i) for i in r)
    if pl%3==0: r = '20' + r
    else: r = '10' + r
    if int(r, 3)<100: res.append(n)
print(max(res))
#18
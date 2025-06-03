def toq(a, q):
    res = ''
    while a:
        res += str(a%q)
        a //= q
    return res[::-1]

m = 0
for n in range(1, 10000):
    r = toq(n, 3)
    if n%3==0: r = '1' + r  + '02'
    else: r += toq(n%3*4, 3)
    if int(r, 3) < 199:
        m = max(m, n)
print(m)
#20
def toq(a, q):
    res = ''
    while a:
        res += str(a%q)
        a //= q
    return res[::-1]
res = []
for n in range(1, 10000):
    r = toq(n, 3)
    if sum(int(i) for i in r)%2==0:
        r = '1' + r + '2'
    else: r = '2' + r + '0'
    r = int(r, 3)
    if r>100: res.append(r)
print(min(res))
#113
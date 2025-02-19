def toq(a, q):
    res = ''
    while a:
        res += str(a%q)
        a //= q
    return res[::-1]

res = []
for n in range(1, 10000):
    r = toq(n, 4)
    if len(r)%2==0:
        r = r[:len(r)//2] + '0' + r[len(r)//2:]
    r = int(r)
    if r <= 180: res.append(n)
print(max(res))
#31
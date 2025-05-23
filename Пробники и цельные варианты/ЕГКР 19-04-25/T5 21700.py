def toq(a, q):
    res = ''
    while a:
        res += str(a%q)
        a //= q
    return res[::-1]

res = []
for n in range(3, 100000):
    r = toq(n, 3)
    if n%3==0: r += r[-2:]
    else: r += toq(n%3*3, 3)
    r = int(r, 3)
    if r<=150: res.append(n)
print(max(res))
#16
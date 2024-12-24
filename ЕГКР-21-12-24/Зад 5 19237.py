def toq(n, q):
    res = ''
    while n:
        res += str(n%q)
        n//=q
    return res[::-1]

res = []
for n in range(1, 1000):
    r  = toq(n, 3)
    if n%3 == 0:
        r += r[-2:]
    else:
        r += toq(sum([int(i) for i in r]),3)
    if int(r, 3) > 220:
        res.append(int(r, 3))
print(min(res))
#222
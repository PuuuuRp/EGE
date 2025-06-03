def toq(a, q):
    res = ''
    while a:
        res += str(a%q)
        a //= q
    return res[::-1]

m = 0
for n in range(3, 1000):
    r = toq(n, 3)
    if n%3==0: r += r[-2:]
    else: r += toq(n%3*3, 3)
    if int(r, 3) <= 150:
        m = n
print(m)
#16
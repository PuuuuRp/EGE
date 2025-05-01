def toq(a, q):
    res = ''
    while a:
        res += str(a%q)
        a //= q
    return res[::-1]

for n in range(1, 1000):
    r = toq(n, 5)
    if len(r)%2==0:
        r = r[len(r)//2:] + r[:len(r)//2]
    else:
        r += str(n%5)
        r = r[len(r)//2:] + r[:len(r)//2]
    r = int(r, 5)
    if r > 50:
        print(n)
        break
#26
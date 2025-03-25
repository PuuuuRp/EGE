from string import ascii_lowercase
def toq(a, q):
    al = '0123456789' + ascii_lowercase
    res = ''
    while a:
        res += al[a%q]
        a//=q
    return res[::-1]

res = []
for n in range(1, 100000):
    r = toq(n, 4)
    if sum(int(i) for i in r)%2==0:
        r += r[-2:]
    else:
        r = '2' + r + '0'
    r = int(r, 4)
    if r>120 and r%2==0:
        res.append(r)
print(min(res))
#136
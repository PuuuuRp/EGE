def toq(a, q):
    res = ''
    while a:
        res += str(a%q)
        a//=q
    return res[::-1]
for n in range(1, 1000):
    r = toq(n, 3)
    if sum(int(i) for i in r)%2==0: r = '12' + r[2:] + '0'
    else: r = '10' + r[2:] + '2'
    if int(r, 3)>105:
        print(n)
        break
#28
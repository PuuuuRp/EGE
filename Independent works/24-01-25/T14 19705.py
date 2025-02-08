def toq(a, q):
    res = ''
    while a:
        res += str(a%q)
        a //= q
    return res[::-1]

for x in range(1, 2006):
    a = toq(43**56 + 113**841 - x, 4)
    ch = (a.count('0')+a.count('2'))%2==0
    nch = (a.count('1')+a.count('3'))%2==0
    n_2 = a.count('2') <= 712
    if ch and nch and n_2: print(x)
#2001
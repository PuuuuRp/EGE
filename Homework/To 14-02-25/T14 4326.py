def toq(a, q):
    al = '0123456789abcde'
    res = ''
    while a:
        res += al[a%q]
        a //= q
    return res[::-1]

a = 3*15**1140 + 2*15**1025 + 15**923 - 3*15**85 + 2*15**74 + 3
st = toq(a, 15)
cnt = 1
m = 0
for i in range(len(st)-1):
    p1, p2 = st[i: i+2]
    if p1==p2: cnt += 1
    else:
        m = max(m, cnt)
        cnt = 1
print(m)
#836
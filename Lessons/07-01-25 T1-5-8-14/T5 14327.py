res = []
for n in range(1, 1000):
    r = oct(n)[2:]
    if n%2 == 0:
        r += oct(list(set(int(i) for i in r))[-1])[2:]
    else:
        r += oct(list(set(int(i) for i in r))[0]*2)[2:]
    if int(r, 8) < 313:
        res.append(n)
print(res[-1])
#38
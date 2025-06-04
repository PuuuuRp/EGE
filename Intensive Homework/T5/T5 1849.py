res = []
for n in range(1, 1000):
    r = bin(n)[2:]
    if n%2==0: r = '1' + r + '0'
    else: r = '11' + r + '11'
    if int(r, 2) > 52: res.append(int(r, 2))
print(min(res))
#56
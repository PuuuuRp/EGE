m = 10**18
for n in range(28, 10000):
    r = bin(n)[2:]
    if r.count('1')%2==0: r = '10' + r[2:] + '0'
    else: r = '11' + r[2:] + '1'
    m = min(int(r, 2), m)
print(m)
#42
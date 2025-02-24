res = []
for n in range(1, 1000):
    r = bin(n)[2:]
    if r.count('1')%2==0: r += '11'
    else: r += '01'
    r = int(r, 2)
    if r>61: res.append(r)
print(min(res))
#63
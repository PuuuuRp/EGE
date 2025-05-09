res = []
for n in range(100, 1001):
    r = bin(n)[2:]
    r = r.replace('0', '')
    res.append(int(r, 2))
print(len(set(res)))
#9
res = []
for n in range(1, 10000):
    r = bin(n)[2:]
    r += str(r.count('1')%2)
    r += str(r.count('1')%2)
    if int(r, 2) > 75:
        res.append(int(r, 2))
print(min(res))
#78
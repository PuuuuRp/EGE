res = []
for A in range(1, 1000):
    if all((z%115==0 or y%78==0 or x%51==0) <= (x%A==0)\
           for x in range(1, 1000)\
           for y in range(78, 1000, 78)\
           for z in range(115, 1000, 115)):
        res.append(A)
print(max(res))
#1
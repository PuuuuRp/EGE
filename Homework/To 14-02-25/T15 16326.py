res = []
for A in range(1, 1000):
    if all((x%A!=0) <= ((x%14==0) <= (x%4!=0))\
           for x in range(1, 1000)):
        res.append(A)
print(max(res))
#28
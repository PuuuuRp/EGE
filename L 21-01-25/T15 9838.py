res = []
for A in range(1000):
    if all(x+2*y>A or y<x or x<30\
           for x in range(1000)\
           for y in range(1000)):
        res.append(A)
print(res[-1])
#89
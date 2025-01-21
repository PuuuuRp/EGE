res = []
for A in range(1, 1000):
    if all(2*x+y != 70 or x<y or A<x\
           for x in range(0, 1000)\
           for y in range(0, 1000)):
        res.append(A)
print(res[-1])
#23
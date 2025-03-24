res = []
for A in range(1000):
    if all(x+2<=50 or y<x+10 or x>=A\
           for x in range(1,1000)\
           for y in range(1, 1000)):
        res.append(A)
print(max(res))
#49
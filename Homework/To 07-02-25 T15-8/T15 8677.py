res = []
for A in range(1, 1000):
    if all((x%17==0) <= (x not in range(80, 101) or A<x+30)\
           for x in range(1, 1000)):
        res.append(A)
print(max(res))
#114
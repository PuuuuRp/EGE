res = []
for A in range(1000):
    if all(x-y>=39 or y<=x or y>=A-20\
           for x in range(1, 1000)\
           for y in range(1, 1000)):
        res.append(A)
print(max(res))
#22
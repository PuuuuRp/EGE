res = []
for A in range(10000):
    if all(x<7 or y>=3*x+A-20 or x>=34 or y<121\
           for x in range(1000)\
           for y in range(1000)):
        res.append(A)
print(res[-1])
#42
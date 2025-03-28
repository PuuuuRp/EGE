res = []
for A in range(1000):
    if all(x<7 or y>=x*3+A-20 or x>=34 or y<121\
           for x in range(1000)\
           for y in range(1000)):
        res.append(A)
print(max(res))
#42
res = []
for A in range(1, 1000):
    if all(not(x&37==0) or not(x&12==0) or x&A==0\
           for x in range(1, 1000)):
        res.append(A)
print(res[-1])
#45
res = []
for A in range(1, 1000):
    if all(x+y <= 22 or y <= x-6 or y >= A \
           for x in range(1, 1000)\
           for y in range(1, 1000)):
        res.append(A)
print(res[-1])
#9
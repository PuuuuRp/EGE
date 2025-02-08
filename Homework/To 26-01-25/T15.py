res = []
for A in range(-1000, 1000):
    if all((not(x*y > A+13)) <= (28*y > 520 or x*25 > 800)\
           for x in range(1, 100)\
           for y in range(1, 100)):
        res.append(A)
print(max(res))
#-13
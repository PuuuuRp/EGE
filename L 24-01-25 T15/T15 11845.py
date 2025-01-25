c = 0
for A in range(1, 11111):
    if all((A%x==0) <= (x == A or x == 1)\
           for x in range(1, 1000)):
        c += 1
print(c)
#1346
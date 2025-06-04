m = 0
for a in range(1, 1000):
    if all(x%a==0 or (x in range(60, 81)) <= (x%22!=0)\
           for x in range(1, 1000)):
        m = a
print(m)
#66
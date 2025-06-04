m = 0
for a in range(1, 1000):
    if all(x%a==0 or (x in range(70, 91)) <= (x%22!=0)\
           for x in range(1, 1000)):
        m = a
print(m)
#88
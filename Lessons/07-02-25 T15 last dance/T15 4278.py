c = 0
for A in range(1, 1001):
    if all(A%12==0 and ((530%x==0) <= ((A%x!=0) <= (170%x!=0)))\
           for x in range(1, 1000)):
        c += 1
print(c)
#933
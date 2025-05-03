cnt = 0
for A in range(1, 1000):
    if all(A%12==0 and ((530%x==0) <= ((A%x!=0) <= (170%x!=0)))\
           for x in range(1, 1000)):
        cnt += 1
print(cnt)
#16
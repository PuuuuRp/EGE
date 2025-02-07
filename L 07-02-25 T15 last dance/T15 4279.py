for A in range(1, 1000):
    if all((x&1097==0) <= ((x&2047!=0) <= (x&A!=0))\
           for x in range(1, 1000)):
        print(A)
        break
#950
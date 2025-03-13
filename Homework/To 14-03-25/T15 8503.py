for A in range(1000):
    if all((x&52!=0 and x&36==0) <= (x&A!=0)\
           for x in range(1000)):
        print(A)
        break
#16
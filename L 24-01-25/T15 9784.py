for A in range(100):
    if all(x*y<A or x<y or 9<x\
           for x in range(1000)\
           for y in range(1000)):
        print(A)
        break
#82
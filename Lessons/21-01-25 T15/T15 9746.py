for A in range(1, 1000):
    if all(x<A or y<A or x+2*y > 50\
           for x in range(1, 1000)\
           for y in range(1, 1000)):
        print(A)
        break
#17
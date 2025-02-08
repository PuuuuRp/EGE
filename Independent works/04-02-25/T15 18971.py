for A in range(1, 1000):
    if all(y>10 or x*A>y+x\
           for x in range(1, 1000)\
           for y in range(1, 1000)):
        print(A)
        break
#12
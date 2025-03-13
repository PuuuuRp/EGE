for A in range(1000):
    if all(x>=11 or 3*x<y or x*y<A\
           for x in range(1000)\
           for y in range(1000)):
        print(A)
        break
#301
for A in range(10000):
    if all(x**2+y**2 > 1024-x or y < -2*x+A\
           for x in range(10000)\
           for y in range(10000)):
        print(A)
        break
#71
for A in range(1000):
    if all(x-3*y<A or y>400 or x>56\
           for x in range(1, 1000)\
           for y in range(1, 1000)):
        print(A)
        break
#54
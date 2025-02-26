for A in range(1000):
    if all(x<=19 or y<2*x+A-50 or y>17\
           for x in range(1000)\
           for y in range(1000)):
        print(A)
        break
#28
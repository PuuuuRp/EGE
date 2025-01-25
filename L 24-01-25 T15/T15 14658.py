for A in range(1, 10000):
    if all((x%12==0) <= (not(x%42==0)) or x+A>=4096\
           for x in range(1, 10000)):
        print(A)
        break
#4012
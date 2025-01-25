for A in range(1000):
    if all(not(x&79==0) and (x&31==0) <= (not(x&A==0))\
            for x in range(90, 101)):
        print(A)
        break
#32
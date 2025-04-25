for A in range(1, 10**6):
    if all( (x&84653!=0 or x&51763!=0) <= (x&A>0)\
            for x in range(10**6)):
        print(A)
        break
#117439
for A in range(1, 1000):
    if all( (37+A+x+45 == 180) == (A+x+90 == 180 and not(A+23<120)) \
            for x in range(1, 1000)):
        print(A)
        break
#98
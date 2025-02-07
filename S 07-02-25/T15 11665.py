for A in range(1, 1000):
    if all(A+x>700-A and A%100+100%x>50\
           for x in range(1, 1000)):
        print(A)
        break
#351
res = []
for A in range(1, 1000):
    if all((str(x)[-1]!='5' and str(x)[-1]=='4') <= (x>A-11)\
           for x in range(1, 1000)):
        res.append(A)
print(res[-1])
#14
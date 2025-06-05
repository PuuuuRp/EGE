m = 0
for A in range(1000):
    if all(2*x+y!=70 or x<y or A<x\
           for x in range(1000)\
           for y in range(1000)):
        m = A
print(m)
#23
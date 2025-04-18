cnt = 0
for a in range(-1000, 1000):
    if all( (a<x or x**2-7*x+10>0) and (a>=y or y**2+7*y+12>0) \
            for x in range(-100, 100)\
            for y in range(-100, 100)):
        cnt += 1
print(cnt)
#5
from math import *
def c(cl):
    res = []
    for d in cl:
        s = 0
        for d1 in cl:
            s += dist(d, d1)
        res.append([s, d])
    return min(res)[1]

with open('27A_19747.txt') as f:
    st = [list(map(float, i.replace(',', '.').split())) for i in f if i]

cl1 = [[x, y] for x, y in st if y<5]
cl2 = [[x, y] for x, y in st if x<5]
cl3 = [[x, y] for x, y in st if x>5 and y>5]
print(len(st) == len(cl1) + len(cl2) + len(cl3))

cent = [c(i) for i in [cl1, cl2, cl3]]
print(sum(i[0] for i in cent)/len(cent)*100000, sum(i[1] for i in cent)/len(cent)*100000)

#########################################################################################################################

with open('27B_19747.txt') as f:
    st = [list(map(float, i.replace(',', '.').split())) for i in f if i]

cl1 = [[x, y] for x, y in st if y>x and y<10]
cl2 = [[x, y] for x, y in st if y<x and x<10]
cl3 = [[x, y] for x, y in st if y>=x and x>10]
cl4 = [[x, y] for x, y in st if y<x and y<10 and x>10]
cl5 = [[x, y] for x, y in st if y<x and y>10]
print(len(st) == len(cl1) + len(cl2) + len(cl3) + len(cl4) + len(cl5))

cent = [c(i) for i in [cl1, cl2, cl3, cl4, cl5]]
print(sum(i[0] for i in cent)/len(cent)*100000, sum(i[1] for i in cent)/len(cent)*100000)

# 532496 533164
# 1091104 954833
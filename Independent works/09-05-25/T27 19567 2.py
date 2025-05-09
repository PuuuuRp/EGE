from math import *
def c(cl):
    res = []
    for d in cl:
        s = 0
        for d1 in cl:
            s += dist(d, d1)
        res.append([s, d])
    return min(res)[1]

with open('27.13.A_19567.txt') as f:
    st = [list(map(float, i.split())) for i in f if i]

cl1 = [[x, y] for x, y in st if y<-1]
cl2 = [[x, y] for x, y in st if y>-1]

cent = [c(i) for i in [cl1, cl2]]
print(sum(i[0] for i in cent)/2*10000, sum(i[1] for i in cent)/2*10000)

##############################################################################################################

with open('27.13.B_19567.txt') as f:
    st = [list(map(float, i.split())) for i in f if i]

cl1 = [[x, y] for x, y in st if y>x+12]
cl2 = [[x, y] for x, y in st if y<x+12 and y>7 and y>x+4]
cl3 = [[x, y] for x, y in st if y<x+12 and y<7 and y>x+4]
cl4 = [[x, y] for x, y in st if y>4 and y<x+4]
cl5 = [[x, y] for x, y in st if y<4 and y<x+4 and y>x-2]
cl6 = [[x, y] for x, y in st if y<x-2 and y<3]

cent = [c(i) for i in [cl1, cl2, cl3, cl4, cl5, cl6]]
print(sum(i[0] for i in cent)/6*10000, sum(i[1] for i in cent)/6*10000)

# 10770 8264
# 3785 46909
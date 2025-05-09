from math import *
def c(cl):
    res = []
    for d in cl:
        s = 0
        for d1 in cl:
            s += dist(d, d1)
        res.append([s, d])
    return min(res)[1]

with open('27_A_21599.txt') as f:
    st = [list(map(float, i.replace(',', '.').split())) for i in f if i]

cl1 = [[x, y] for x, y in st if y<-5]
cl2 = [[x, y] for x, y in st if y>-5 and y<x-10]
cl3 = [[x, y] for x, y in st if y>x-10]

cent = [c(i) for i in [cl1, cl2, cl3]]
print(sum(i[0] for i in cent)/3*10000, sum(i[1] for i in cent)/3*10000)

######################################################################################################

with open('27_B_21599.txt') as f:
    st = [list(map(float, i.replace(',', '.').split())) for i in f if i]

print(len(st))
eps = 1.7
clus = []
while st:
    cl = [st.pop()]
    for d in cl:
        for d1 in st.copy():
            if dist(d, d1)<eps:
                cl.append(d1)
                st.remove(d1)
    print(len(cl))
    clus.append(cl)
print(sum(len(i) for i in clus))

cent = [c(i) for i in clus]
print(sum(i[0] for i in cent)/6*10000, sum(i[1] for i in cent)/6*10000)

# 178755 2896
# 37392 50998
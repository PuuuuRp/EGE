from math import *
# from turtle import *
# tracer(0)
def c(cl):
    res = []
    for d in cl:
        s = 0
        for d1 in cl:
            s += dist(d, d1)
        res.append([s, d])
    return max(res)[1]

with open('27.19.B_20497.txt') as f:
    st = [list(map(float, i.split())) for i in f if i]

print(len(st))
eps = 2
clus = []
while st:
    cl = [st.pop()]
    for d in cl:
        for d1 in st:
            if dist(d, d1)<eps:
                cl.append(d1)
                st.remove(d1)
    print(len(cl))
    if len(cl)>10:
        clus.append(cl)

# m = 30
# col = ['red', 'green', 'blue']
# up()
# for cl, c in zip(clus, col):
#     for d in cl:
#         goto(d[0]*m, d[1]*m)
#         dot(3, c)
# done()

cent = [c(i) for i in clus]
print(sum(i[0] for i in cent)/5*10000, sum(i[1] for i in cent)/5*10000)

# 13258 2656
# -209434 474989
from math import *
def c(cl):
    res = []
    for d in cl:
        s = 0
        for d1 in cl:
            s += dist(d, d1)
        res.append([s, d])
    return min(res)[1]

with open('2709_B.txt') as f:
    st = [list(map(float, i.split())) for i in f if i]

eps = 0.6
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

cent = [[len(i), c(i)] for i in clus]
print(min(cent)[1][0]*10000, max(cent)[1][1]*10000)

# 51823 3238
# 57528 61605
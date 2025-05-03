from math import *
def c(cl):
    res = []
    for d in cl:
        s = 0
        for d1 in cl:
            s += dist(d, d1)
        res.append([s, d])
    return min(res)[1]

with open('27B_18623.txt') as f:
    st = [list(map(float, i.replace(',', '.').split())) for i in f if i]

print(len(st))
eps = 1
clus = []
while st:
    cl = [st.pop()]
    for d in cl:
        for d1 in st.copy():
            if dist(d, d1)<eps:
                cl.append(d1)
                st.remove(d1)
    clus.append(cl)
print([len(i) for i in clus])

cent = [c(i) for i in clus]
print(sum(i[0] for i in cent)/len(cent)*100000, sum(i[1] for i in cent)/len(cent)*100000)

#398800 348577
#596884 400991
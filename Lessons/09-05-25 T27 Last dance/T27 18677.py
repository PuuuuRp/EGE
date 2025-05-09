from math import *
def c(cl):
    res = []
    for d in cl:
        s = 0
        for d1 in cl:
            s += dist(d, d1)
        res.append([s, d])
    return min(res)[1]

with open('27B_18677.txt') as f:
    st = [list(map(float, i.replace(',', '.').split())) for i in f if i]

print(len(st))
eps = 0.7
s = 0
clus = []
while st:
    cl = [st.pop()]
    for d in cl:
        for d1 in st.copy():
            if dist(d, d1)<eps:
                cl.append(d1)
                st.remove(d1)
    print(len(cl))
    s += len(cl)
    if len(cl)>10:
        clus.append(cl)
print(s)

cent = [c(i) for i in clus]
print(sum(i[0] for i in cent)/3*100000, sum(i[1] for i in cent)/3*100000)

# 528073 71781
# 669946 370701
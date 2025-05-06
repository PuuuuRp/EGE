from math import *
def c(cl):
    res = []
    for d in cl:
        s = 0
        for d1 in cl:
            s += dist(d, d1)
        res.append([s, d])
    return min(res)[1]

with open('2710_B.txt') as f:
    st = [list(map(float, i.split())) for i in f if i]

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
    print(len(cl))
    if len(cl)>10:
        clus.append(cl)

cent = [c(i) for i in clus]
print(sum(i[0] for i in cent)/3*10000, sum(i[1] for i in cent)/3*10000)

# 5949 27762
# 7455 6872
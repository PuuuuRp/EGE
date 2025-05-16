from math import *
def c(cl):
    res = []
    for d in cl:
        s = 0
        for d1 in cl:
            s += dist(d, d1)
        res.append([s, d])
    return min(res)[1]

with open('27_B_18884.txt') as f:
    st = [list(map(int, i.split())) for i in f if i]

print(len(st))
s = 0
eps = 5
clus = []
while st:
    cl = [st.pop()]
    for d in cl:
        for d1 in st.copy():
            if dist(d, d1)<eps:
                cl.append(d1)
                st.remove(d1)
    s += len(cl)
    print(len(cl))
    clus.append(cl)
print(s)

cent = [c(i) for i in clus]
print(sum(i[0] for i in cent)/3, sum(i[1] for i in cent)/3)

# 40 30
# 19 176
from math import *
def c(cl):
    res = []
    for d in cl:
        s = 0
        for d1 in cl:
            s += dist(d, d1)
        res.append([s, d])
    return max(res)[1]

with open('27.17.B_19566.txt') as f:
    st = [list(map(float, i.split())) for i in f if i]

print(len(st))
eps = 1
s = 0
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
    if len(cl)>15: clus.append(cl)
print(s)

cent = [c(i) for i in clus]
print(sum(i[0] for i in cent)/4*10000,
      sum(i[1] for i in cent)/4*10000)

# 14803 51534
# 216297 43456
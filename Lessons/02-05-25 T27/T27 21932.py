from math import *
def cent(cl):
    res = []
    for d in cl:
        s = 0
        for d1 in cl:
            s += dist(d, d1)
        res.append([s, d])
    return min(res)[1]

with open('27_B_21932.txt') as f:
    st = [list(map(float, i.replace(',', '.').split())) for i in f if i]

print(len(st))
eps = 1
clus = []
while st:
    cl = [st.pop()]
    for d in cl:
        for d1 in st.copy():
            if dist(d, d1) < eps:
                cl.append(d1)
                st.remove(d1)
    clus.append([len(cl), cl])

print([i[0] for i in clus])

print(cent(min(clus)[1])[0]*10000, cent(max(clus)[1])[1]*10000)

# 32865 70666
# 144062 61170
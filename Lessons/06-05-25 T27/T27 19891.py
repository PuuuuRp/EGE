from math import *
def c(cl):
    res = []
    for x, y in cl:
        s  = 0
        for a, b in cl:
            s += max(abs(x-a), abs(y-b))
        res.append([s, [x, y]])
    return min(res)[1]

with open('27.3.B_19891.txt') as f:
    st = [list(map(float, i.split())) for i in f if i]

# cl1 = [[x, y] for x, y in st if x>3]
# cl2 = [[x, y] for x, y in st if x<3]
#
# cent = [c(i) for i in [cl1, cl2]]

eps = 0.8
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

cent = [c(i) for i in clus]
print(sum(i[0] for i in cent)/4*10000, sum(i[1] for i in cent)/4*10000)

#31889 4751
#23102 4049
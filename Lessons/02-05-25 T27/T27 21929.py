from math import *
def c(cl):
    res = []
    for d in cl:
        s = 0
        for d1 in cl:
            s += dist(d, d1)
        res.append([s, d])
    return min(res)[1]

with open('27_B_21929.txt') as f:
    st = [list(map(float, i.replace(',', '.').split())) for i in f if i]

eps = 1
arr = []
while st:
    cl = [st.pop()]
    for d in cl:
        for d1 in st.copy():
            if dist(d, d1)<eps:
                cl.append(d1)
                st.remove(d1)
    arr.append(cl)

print([len(i) for i in arr])

cent = [c(i) for i in arr]
print(sum(i[0] for i in cent)/len(cent)*10000, \
      sum(i[1] for i in cent)/len(cent)*10000)

#45336 117141
#167659 143170
from math import dist
def cent(cl):
    res = []
    for d in cl:
        s = 0
        for d1 in cl:
            s += dist(d, d1)
        res.append([s, d])
    return min(res)[1]

with open('27_A_21720.txt') as f:
    st = [list(map(float, i.replace(',', '.').split())) for i in f if i]

eps = 2
clus = []
while st:
    cl = [st.pop()]
    for d in cl:
        for d1 in st.copy():
            if dist(d, d1) < eps:
                cl.append(d1)
                st.remove(d1)
    clus.append(cl)

print([len(cl) for cl in clus])

center = [cent(i) for i in clus]
print(sum(i[0] for i in center)/len(center)*10000, sum(i[1] for i in center)/len(center)*10000)

#######################################################################################################

with open('27_B_21720.txt') as f:
    st = [list(map(float, i.replace(',', '.').split())) for i in f if i]

eps = 2
clus = []
while st:
    cl = [st.pop()]
    for d in cl:
        for d1 in st.copy():
            if dist(d, d1) < eps:
                cl.append(d1)
                st.remove(d1)
    clus.append(cl)
print([len(cl) for cl in clus])

center = [cent(i) for i in clus]
print(sum(i[0] for i in center) / len(center) * 10000, sum(i[1] for i in center) / len(center) * 10000)

# 32540 13646
# 47031 25263
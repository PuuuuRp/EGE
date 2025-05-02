from math import dist
def cent(cl):
    res = []
    for x, y in cl:
        s = 0
        for a,b in cl:
            s += dist([x, y], [a, b])
        res.append([s, [x, y]])
    return min(res)[1]

with open('27_A_21911.txt') as f:
    st = [list(map(float, i.replace(',','.').split())) for i in f if i]

eps = 2
clus = []
while st:
    cl = [st.pop()]
    for x, y in cl:
        for a,b in st.copy():
            if dist([x, y], [a, b]) < eps:
                cl.append([a, b])
                st.remove([a, b])
    clus.append(cl)

print([len(cl) for cl in clus])

c1 = cent(clus[0])
c2 = cent(clus[1])

print((c1[0] + c2[0])/2*10000, (c1[1] + c2[1])/2*10000)

###########################################################

with open('27_B_21911.txt') as f:
    st = [list(map(float, i.replace(',','.').split())) for i in f if i]

eps = 2
clus = []
while st:
    cl = [st.pop()]
    for x, y in cl:
        for a,b in st.copy():
            if dist([x, y], [a, b]) < eps:
                cl.append([a, b])
                st.remove([a, b])
    clus.append(cl)

print([len(cl) for cl in clus])

c1 = cent(clus[0])
c2 = cent(clus[1])
c3 = cent(clus[2])

print((c1[0] + c2[0] + c3[0])/3*10000, (c1[1] + c2[1] + c3[1])/3*10000)

# 26216 24182
# 150891 63754
def cent(cl):
    res = []
    for x, y in cl:
        s = 0
        for a, b in cl:
            s += ((x-a)**2 + (y-b)**2)**.5
        res.append([s,[x, y]])
    return min(res)[1]
with open('27_A_17916.txt') as f:
    st = [list(map(float, i.replace(',', '.').split())) for i in f if i]

cl1 = [[x, y] for x, y in st if y>8]
cl2 = [[x, y] for x, y in st if y<8]

c1 = cent(cl1)
c2 = cent(cl2)

print((c1[0] + c2[0])/2*10000, (c1[1] + c2[1])/2*10000)

##################################################

with open('27_B_17916.txt') as f:
    st = [list(map(float, i.replace(',', '.').split())) for i in f if i]

cl1 = [[x, y] for x, y in st if y>14]
cl2 = [[x, y] for x, y in st if 10<y<13]
cl3 = [[x, y] for x, y in st if 5<y<9]
cl4 = [[x, y] for x, y in st if y<4 and x<7]
cl5 = [[x, y] for x, y in st if x>13]

c1 = cent(cl1)
c2 = cent(cl2)
c3 = cent(cl3)
c4 = cent(cl4)
c5 = cent(cl5)

print((c1[0] + c2[0] + c3[0]+ c4[0]+ c5[0])/5*10000, (c1[1] + c2[1] + c3[1]+ c4[1]+ c5[1])/5*10000)

# 119766 83062
# 90275 74960
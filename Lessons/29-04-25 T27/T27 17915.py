with open('27_A_17915.txt') as f:
    st = [list(map(float, i.replace(',', '.').split())) for i in f if i]

cl1 = [[x, y] for x, y in st if y<23 and x>12]
cl2 = [[x, y] for x, y in st if y>23 and x>7]
cl3 = [[x, y] for x, y in st if x<7]

def cent(cl):
    res = []
    for x, y in cl:
        s = 0
        for a, b in cl:
            s += ( (x-a)**2 + (y-b)**2 )**.5
        res.append([s, [x, y]])
    return min(res)[1]

c1 = cent(cl1)
c2 = cent(cl2)
c3 = cent(cl3)

print((c1[0] + c2[0] + c3[0])/3*10000, (c1[1] + c2[1] + c3[1])/3*10000)

########################################################

with open('27_B_17915.txt') as f:
    st = [list(map(float, i.replace(',', '.').split())) for i in f if i]

cl1 = [[x, y] for x, y in st if y<13 and x>15.5]
cl2 = [[x, y] for x, y in st if y<13 and x<15.5]
cl3 = [[x, y] for x, y in st if x<22 and y>15]
cl4 = [[x, y] for x, y in st if x>22]

def cent(cl):
    res = []
    for x, y in cl:
        s = 0
        for a, b in cl:
            s += ( (x-a)**2 + (y-b)**2 )**.5
        res.append([s, [x, y]])
    return min(res)[1]

c1 = cent(cl1)
c2 = cent(cl2)
c3 = cent(cl3)
c4 = cent(cl4)

print((c1[0] + c2[0] + c3[0] + c4[0])/4*10000, (c4[0] + c1[1] + c2[1] + c3[1])/4*10000)

# 95200 233468
# 163215 147061
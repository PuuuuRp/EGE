with open('27_A_21425.txt') as f:
    st = [list(map(float, i.replace(',', '.').split())) for i in f if i]

cl1 = [[x, y] for x, y in st if x>17]
cl2 = [[x, y] for x, y in st if x<17]
print(len(st) == len(cl1) + len(cl2))

def cent(cl):
    res = []
    for x, y in cl:
        s = 0
        for a, b in cl:
            s += ((x-a)**2 + (y-b)**2)**.5
        res.append([s, [x, y]])
    return min(res)[1]

c1 = cent(cl1)
c2 = cent(cl2)

print((c1[0] + c2[0])/2*10000, (c1[1] + c2[1])/2*10000)

###############################################################

with open('27_B_21425.txt') as f:
    st = [list(map(float, i.replace(',', '.').split())) for i in f if i]

cl1 = [[x, y] for x, y in st if x>22]
cl2 = [[x, y] for x, y in st if 6<x<22]
cl3 = [[x, y] for x, y in st if x<6]
print(len(st) == len(cl1) + len(cl2) + len(cl3))

def cent(cl):
    res = []
    for x, y in cl:
        s = 0
        for a, b in cl:
            s += ((x-a)**2 + (y-b)**2)**.5
        res.append([s, [x, y]])
    return min(res)[1]

c1 = cent(cl1)
c2 = cent(cl2)
c3 = cent(cl3)

print((c1[0] + c2[0] + c3[0])/3*10000, (c1[1] + c2[1]+ c3[1])/3*10000)

# 167990 73043
# 122627 29105
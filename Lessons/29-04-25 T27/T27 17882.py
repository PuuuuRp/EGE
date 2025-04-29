with open('27_A_17882.txt') as f:
    st = [list(map(float, i.split())) for i in f if i]

cl1 = [[x, y] for x, y in st if y>-2*x+4]
cl2 = [[x, y] for x, y in st if y<-2*x+4]

def cent(cl):
    res = []
    for x, y in cl:
        s = 0
        for a, b in cl:
            s += ( (x-a)**2 + (y-b)**2 )**.5
        res.append([s, [x, y]])
    return min(res)

c1 = cent(cl1)[1]
c2 = cent(cl2)[1]

print((c1[0] + c2[0])/2*10000, (c1[1] + c2[1])/2*10000)

#########################################

with open('27_B_17882.txt') as f:
    st = [list(map(float, i.split())) for i in f if i]

cl1 = [[x, y] for x, y in st if y<-2*x+8]
cl2 = [[x, y] for x, y in st if y>-2*x+8 and x<5]
cl3 = [[x, y] for x, y in st if y>-2*x+8 and x>5]

def cent(cl):
    res = []
    for x, y in cl:
        s = 0
        for a, b in cl:
            s += ( (x-a)**2 + (y-b)**2 )**.5
        res.append([s, [x, y]])
    return min(res)

c1 = cent(cl1)[1]
c2 = cent(cl2)[1]
c3 = cent(cl3)[1]

print((c1[0] + c2[0] + c3[0])/3*10000, (c3[1] + c1[1] + c2[1])/3*10000)
#10738 30730
#37522 51277
from math import *
def c(cl):
    res = []
    for d in cl:
        s = 0
        for d1 in cl:
            s += dist(d, d1)
        res.append([s, d])
    return max(res)[1]

with open('27_A_21931.txt') as f:
    st = [list(map(float, i.replace(',', '.').split())) for i in f if i]

cl1 = [[x, y] for x, y in st if y<10]
cl2 = [[x, y] for x, y in st if y>10]

print(len(st))
print(len(cl1), len(cl2))

cent = [[len(i), c(i)] for i in [cl1, cl2]]
print(min(cent)[1][0]*10000, max(cent)[1][1]*10000)

#######################################################################################

with open('27_B_21931.txt') as f:
    st = [list(map(float, i.replace(',', '.').split())) for i in f if i]

cl1 = [[x, y] for x, y in st if y<10]
cl2 = [[x, y] for x, y in st if y>10 and x>17]
cl3 = [[x, y] for x, y in st if y>10 and x<17]

print(len(st))
print(len(cl1), len(cl2), len(cl3))

cent = [[len(i), c(i)] for i in [cl1, cl2, cl3]]
print(min(cent)[1][0]*10000, max(cent)[1][1]*10000)

# 1663 61127
# 147474 61934
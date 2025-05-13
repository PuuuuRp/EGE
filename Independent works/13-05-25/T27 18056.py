from math import *
from turtle import *
tracer(0)
screensize(1500, 1500)
def c(cl):
    res = []
    for d in cl:
        s = 0
        for d1 in cl:
            s += dist(d, d1)
        res.append([s, d])
    return min(res)[1]

def t(clus, col):
    m = 100
    up()
    for cl, c in zip(clus, col):
        for x, y in cl:
            goto(m*x, m*y)
            dot(3, c)
    done()

# with open('27B_18056.txt') as f:
#     st = [list(map(float, i.replace(',', '.').split())) for i in f if i]
#
# print(len(st))
# eps = 0.8
# s = 0
# clus = []
# while st:
#     cl = [st.pop()]
#     for d in cl:
#         for d1 in st.copy():
#             if dist(d, d1)<eps:
#                 cl.append(d1)
#                 st.remove(d1)
#     s += len(cl)
#     print(len(cl))
#     if len(cl)>15:
#         clus.append(cl)
# print(s)
#
# t(clus, ['red', 'blue', 'green'])
#
# cent = [c(i) for i in clus]
# print(sum(i[0] for i in cent)/3*10**5, sum(i[1] for i in cent)/3*10**5)

# 43744 47901
# 99895 100091

####################################################################################

# with open('27A_18056.txt') as f:
#     st = [list(map(float, i.replace(',', '.').split())) for i in f if i]
#
# cl1 = [[x, y] for x, y in st if y>-1 and x<0.5]
# cl2 = [[x, y] for x, y in st if y<-1 and x>0.5]
#
# t([cl1, cl2], ['red', 'blue', 'green'])
#
# cent = [c(i) for i in [cl1, cl2]]
# print(sum(i[0] for i in cent)/2*10**5, sum(i[1] for i in cent)/2*10**5)

# 43744 47901

#######################################################################################

with open('27B_18056.txt') as f:
    st = [list(map(float, i.replace(',', '.').split())) for i in f if i]

cl1 = [[x, y] for x, y in st if y>-2*x+4 and y>0 and x<4]
cl2 = [[x, y] for x, y in st if y<-2*x+4 and y<4 and y>-2]
cl3 = [[x, y] for x, y in st if y<0 and x>0.3]

print(len(st) - sum(len(i) for i in [cl1, cl2, cl3]))

t([cl1, cl2, cl3], ['red', 'blue', 'green'])

cent = [c(i) for i in [cl1, cl2, cl3]]
print(sum(i[0] for i in cent)/3*10**5, sum(i[1] for i in cent)/3*10**5)
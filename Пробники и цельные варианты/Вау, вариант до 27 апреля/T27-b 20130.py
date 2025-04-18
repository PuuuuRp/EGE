with open('27B_20130.txt') as f:
    st = [list(map(float, i.replace(',', '.').split())) for i in f if i]

cl_1 = [[x, y] for x, y in st if x > 6]
cl_2 = [[x, y] for x, y in st if y > 6 and x < 4]
cl_3 = [[x, y] for x, y in st if y < 6 and x < 4]

def cent(cl):
    res = []
    for x, y in cl:
        s = 0
        for a, b in cl:
            res.append([((x - a) ** 2 + (y - b) ** 2) ** .5, [x, y], [a, b]])
    return max(res)

c1, c11 = cent(cl_1)[1:]
c2, c22 = cent(cl_2)[1:]
c3, c33 = cent(cl_3)[1:]

print((c1[0]+c2[0]+c3[0]+c11[0]+c22[0]+c33[0])/6*10000, (c1[1]+c2[1]+c3[1]+c11[1]+c22[1]+c33[1])/6*10000)
#23982 47539
with open('27A_20130.txt') as f:
    st = [list(map(float, i.replace(',', '.').split())) for i in f if i]

cl_1 = [[x, y] for x, y in st if y > 6]
cl_2 = [[x, y] for x, y in st if y < 6]

def cent(cl):
    res = []
    for x, y in cl:
        for a, b in cl:
             res.append([((x-a)**2 + (y-b)**2)**.5, [x, y], [a, b]])
    return max(res)

c1, c11 = cent(cl_1)[1:]
c2, c22 = cent(cl_2)[1:]

print((c1[0]+c11[0]+c22[0]+c2[0])/4*10000, (c1[1]+c11[1]+c22[1]+c2[1])/4*10000,)
#16730 48696
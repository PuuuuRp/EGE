with open('27B_18050.txt') as f:
    stars = [list(map(float, i.replace(',', '.').split())) for i in f.readlines() if i]

cl_1 = [[x, y] for x, y in stars if y < x+3 and y < -2*x+20]
cl_2 = [[x, y] for x, y in stars if y > x+3 and y < -2*x+20]
cl_3 = [[x, y] for x, y in stars if y < 2*x-1.5 and y > -2*x+20]

def cent(cl):
    res = []
    for x, y in cl:
        s = 0
        for x1, y1 in cl:
            s += ((x1-x)**2 + (y1-y)**2)**.5
        res.append([s, [x, y]])
    return min(res)

c_1 = cent(cl_1)[1]
c_2 = cent(cl_2)[1]
c_3 = cent(cl_3)[1]

print((c_1[0]+c_2[0]+c_3[0])/3*10000, (c_1[1]+c_2[1]+c_3[1])/3*10000)
#53088 78127
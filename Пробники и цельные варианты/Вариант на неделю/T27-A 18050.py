with open('27A_18050.txt') as f:
    stars = [list(map(float, i.replace(',', '.').split())) for i in f.readlines() if i]
cl_1 = [[x, y] for x, y in stars if 0.5<=x<=2.7 and 3<=y<=5.8]
cl_2 = [[x, y] for x, y in stars if -1.6<=x<=0.7 and 0.5<=y<=3.4]

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

print((c_1[0]+c_2[0])/2*10000, (c_1[1]+c_2[1])/2*10000)
#5317 32715
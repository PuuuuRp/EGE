with open('27_A_20816.txt') as f:
    arr = [list(map(float, i.replace(',', '.').split())) for i in f.readlines() if i]
cl_1 = [i for i in arr if 0<=i[0]<=6 and 4<=i[1]<=10]
cl_2 = [i for i in arr if -8<=i[0]<=0 and -10<=i[1]<=0]

def center(cl):
    res = []
    for star in cl:
        suma = 0
        for anot in cl:
            suma += ((star[0]-anot[0])**2 + (star[1]-anot[1])**2)**.5
        res.append([suma, star])
    return min(res)

c_1 = center(cl_1)[1]
c_2 = center(cl_2)[1]

x1, y1 = c_1
x2, y2 = c_2
print((x1+x2)/2*10000)
print((y1+y2)/2*10000)
#10592 6300
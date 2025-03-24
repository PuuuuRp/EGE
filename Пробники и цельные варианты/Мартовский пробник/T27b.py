with open('27_B_20816.txt') as f:
    arr = [list(map(float, i.replace(',', '.').split())) for i in f.readlines() if i]
cl_1 = [i for i in arr if -15<=i[0]<=-5 and -10<=i[1]<=0]
cl_2 = [i for i in arr if -5<=i[0]<=10 and -15<=i[1]<=-5]
cl_3 = [i for i in arr if -3<=i[0]<=8 and -3<=i[1]<=8]

print(len(arr), len(cl_1)+len(cl_2)+len(cl_3))

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
c_3 = center(cl_3)[1]

x1, y1 = c_1
x2, y2 = c_2
x3, y3 = c_3
print((x1+x2+x3)/3*10_000)
print((y1+y2+y3)/3*10_000)
#15981
#37287
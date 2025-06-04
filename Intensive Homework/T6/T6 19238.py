from turtle import *
tracer(0)
screensize(1500, 1500)
m = 15
lt(90)

for i in range(8):
    fd(m*16)
    rt(90)
    fd(m*22)
    rt(90)
up()
fd(m * 5)
rt(90)
fd(m * 5)
lt(90)
down()
for i in range(8):
    fd(m*52)
    rt(90)
    fd(m*77)
    rt(90)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(m*x, m*y)
        dot(3, 'red')
done()
#17*11 = 187
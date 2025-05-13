from turtle import *
tracer(0)
screensize(1500, 1500)
m = 20
lt(90)
for i in range(2):
    fd(m*6)
    rt(90)
    fd(12*m)
    rt(90)
up()
bk(m*3)
lt(90)
fd(m*5)
rt(90)
down()
for i in range(4):
    fd(m * 6)
    rt(90)
up()
fd(8*m)
down()
for i in range(4):
    fd(m * 8)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(m*x, m*y)
        dot(3, 'red')
done()
#164
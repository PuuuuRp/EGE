from turtle import *
tracer(0)
screensize(1500, 1500)
m = 15
lt(90)
for i in range(9):
    fd(m * 17)
    lt(90)
    fd(m * 8)
    lt(90)
    fd(17*m)
up()
lt(90)
fd(m*3)
rt(90)
fd(m*5)
lt(90)
down()
for i in range(4):
    fd(m * 97)
    rt(90)
    fd(m * 132)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(m*x, m*y)
        dot(3, 'red')
done()
#
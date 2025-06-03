from turtle import *
tracer(0)
screensize(1500, 1500)
lt(90)
m = 15

for i in range(9):
    fd(m*27)
    rt(90)
    fd(m*30)
    rt(90)
up()
fd(m * 3)
rt(90)
fd(m * 6)
lt(90)
down()
for i in range(9):
    fd(m*77)
    rt(90)
    fd(m*66)
    rt(90)

up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(m*x, m*y)
        dot(3, 'white')
done()
#96
from turtle import *
tracer(0)
screensize(1700, 1700)
lt(90)
m = 19
for i in range(4):
    fd(16*m)
    lt(90)
    fd(20*m)
    lt(90)
up()
fd(4*m)
lt(90)
fd(8*m)
rt(180)
down()
for i in range(3):
    fd(35*m)
    lt(90)
    fd(6*m)
    lt(90)
up()
for x in range(-60, 60):
    for y in range(-60, 60):
        goto(m*x, m*y)
        dot(4, 'red')
done()
#126
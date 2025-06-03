from turtle import *
tracer(0)
lt(90)
screensize(1500, 1500)
m = 15

for i in range(3):
    fd(m*7)
    rt(90)
    fd(m*12)
    rt(90)
up()
fd(m * 4)
rt(90)
fd(m * 6)
lt(90)
down()
for i in range(4):
    fd(m*83)
    rt(90)
    fd(m*77)
    rt(90)

up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(m*x, m*y)
        dot(3, 'red')
done()
#4*13 + 6*4 + 84*78 = 6628
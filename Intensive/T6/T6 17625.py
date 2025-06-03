from turtle import *
tracer(0)
screensize(1500, 1500)
lt(90)
m = 15

for i in range(10):
    fd(22*m)
    rt(90)
    fd(15*m)
    rt(90)
up()
fd(1 * m)
rt(90)
fd(1 * m)
lt(90)
down()
for i in range(10):
    fd(72*m)
    rt(90)
    fd(79*m)
    rt(90)

up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(m*x, m*y)
        dot(3, 'white')
done()
#21 + 15 + 14 + 2 + 20 = 72
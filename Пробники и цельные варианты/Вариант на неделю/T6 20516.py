from turtle import *
tracer(0)
screensize(1500, 1500)
m = 20
lt(90)
for i in range(3):
    fd(2*m)
    rt(90)
    fd(3 * m)
    lt(90)

rt(180)
fd(6*m)
rt(90)
fd(9*m)

up()
bk(3*m)
rt(90)
down()

for i in range(2):
    fd(m)
    rt(90)
    fd(2 * m)
    lt(90)

rt(180)
fd(3*m)
rt(90)
fd(4*m)
rt(90)
fd(m)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(m*x, m*y)
        dot(3, 'red')
done()
#12
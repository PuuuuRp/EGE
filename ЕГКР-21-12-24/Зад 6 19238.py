from turtle import *
screensize(1500, 1500)
tracer(0)
m = 15
lt(90)

for i in range(8):
    fd(16*m)
    rt(90)
    fd(22 * m)
    rt(90)
up()
fd(5*m)
rt(90)
fd(5*m)
lt(90)
down()
for i in range(8):
    fd(52*m)
    rt(90)
    fd(77 * m)
    rt(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(m*x, m*y)
        dot(3, 'purple')
done()
#187
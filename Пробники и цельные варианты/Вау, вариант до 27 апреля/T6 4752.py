from turtle import *
tracer(0)
screensize(1000, 1000)
m = 20
lt(90)
for i in range(15):
    fd(m*4)
    rt(60)

teleport(0, 0)
rt(180)
fd(20*m)
teleport(0, 0)
lt(270)
fd(20*m)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(m*x, m*y)
        dot(3, 'purple')
done()
#28
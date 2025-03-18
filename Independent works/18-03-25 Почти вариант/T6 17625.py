from turtle import *
tracer(0)
screensize(1500, 1500)
m = 15
lt(90)
for i in range(10):
    fd(m*22)
    rt(90)
    fd(16*m)
    rt(90)
up()
fd(m)
rt(90)
fd(m)
lt(90)
down()
for i in range(10):
    fd(m*72)
    rt(90)
    fd(79*m)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(m*x, m*y)
        dot(3, 'red')
done()
#72
from turtle import *
tracer(0)
screensize(1500, 1500)
m = 30
lt(90)

rt(30)
for i in range(3):
    rt(150)
    fd(6*m)
    rt(30)
    fd(m*12)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(m*x, m*y)
        dot(3, 'red')
done()
#30
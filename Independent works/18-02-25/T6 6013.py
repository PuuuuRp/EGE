from turtle import *
tracer(0)
screensize(1000, 1000)
m = 15
lt(90)
for i in range(2):
    rt(120)
    fd(7*m)
rt(300)
for i in range(2):
    rt(120)
    fd(7*m)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(m*x, m*y)
        dot(3, 'red')
done()
#42
from turtle import *
tracer(0)
screensize(2000, 2000)
m = 20
lt(90)
for i in range(2):
    fd(m*28)
    rt(90)
    fd(m*18)
    rt(90)
up()
fd(m*14)
rt(90)
fd(m*10)
lt(90)
down()
for i in range(2):
    fd(m*30)
    rt(90)
    fd(m*7)
    rt(90)
up()
for x in range(-60, 60):
    for y in range(-60, 60):
        goto(m*x, m*y)
        dot(3, 'red')
done()
#16*8 + 29*19 = 679
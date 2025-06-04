from turtle import *
tracer(0)
screensize(1500, 1500)
m = 15
lt(90)

for i in range(2):
    fd(m*10)
    rt(90)
    fd(m*18)
    rt(90)
up()
fd(m * 5)
rt(90)
fd(m * 7)
lt(90)
down()
for i in range(2):
    fd(m*10)
    rt(90)
    fd(m*7)
    rt(90)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(m*x, m*y)
        dot(3, 'red')
done()
#11*19 + 8*5 = 249
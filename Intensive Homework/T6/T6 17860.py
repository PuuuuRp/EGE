from turtle import *
tracer(0)
screensize(1500, 1500)
m = 15
lt(90)

for x in range(9):
    fd(m*22)
    rt(90)
    fd(m*6)
    rt(90)
up()
fd(m * 1)
rt(90)
fd(m * 5)
lt(90)
down()
for x in range(9):
    fd(m*53)
    rt(90)
    fd(m*75)
    rt(90)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(m*x, m*y)
        dot(3, 'white')
done()
#2 + 21*2 = 44
from turtle import *
tracer(0)
screensize(1500, 1500)
lt(90)
m = 20
for i in range(7):
    fd(m*9)
    rt(90)
    fd(m*16)
    rt(90)

up()
fd(m*3)
rt(90)
fd(m*4)
lt(90)
down()

for i in range(4):
    fd(m * 7)
    rt(90)
    fd(m * 13)
    rt(90)
up()
for x in range(-60, 60):
    for y in range(-60, 60):
        goto(m*x, m*y)
        dot(3, 'red')
done()
#(5 + 13) * 2 = 36
from turtle import *
tracer(0)
screensize(1500, 1500)
m = 15
lt(90)

for i in range(2):
    fd(m*13)
    rt(90)
    fd(m*20)
    rt(90)
up()
fd(m * 8)
rt(90)
bk(m * 3)
lt(90)
down()
for i in range(2):
    fd(m*16)
    rt(90)
    fd(m*8)
    rt(90)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(m*x, m*y)
        dot(3, 'red')
done()
#14*21 + 3*6 + 9*11 = 411
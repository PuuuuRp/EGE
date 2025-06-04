from turtle import *
tracer(0)
screensize(1500, 1500)
m = 15
lt(90)

for i in range(2):
    fd(m*5)
    lt(90)
    bk(m*13)
    lt(90)
up()
bk(m * 10)
rt(90)
fd(m * 9)
lt(90)
down()
for i in range(2):
    fd(m*11)
    rt(90)
    fd(m*7)
    rt(90)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(m*x, m*y)
        dot(3, 'red')
done()
#9*6 + 5*4 + 12*8 = 170
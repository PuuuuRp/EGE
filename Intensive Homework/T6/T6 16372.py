from turtle import *
tracer(0)
screensize(1500, 1500)
m = 15
lt(90)

for i in range(2):
    fd(m*23)
    lt(90)
    bk(27*m)
    lt(90)
up()
bk(m*5)
rt(90)
fd(m*11)
lt(90)
down()
for i in range(2):
    fd(m*26)
    rt(90)
    fd(32*m)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(m*x, m*y)
        dot(3, 'red')
done()
#27*33 + 2*17 + 24*11 = 1189
from turtle import *
tracer(0)
screensize(1500, 1500)
m = 15
lt(90)

for i in range(2):
    fd(m*28)
    rt(90)
    fd(m*18)
    rt(90)
up()
fd(m * 14)
rt(90)
fd(m * 10)
lt(90)
down()
for i in range(2):
    fd(m*30)
    rt(90)
    fd(m*7)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(m*x, m*y)
        dot(3, 'red')
done()
#29 * 19 + 8*16 = 679
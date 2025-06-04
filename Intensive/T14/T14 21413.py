from string import *
al = '0123456789' + ascii_lowercase

for x in al[:21]:
    a = int(f'82934{x}2', 21)
    b = int(f'2924{x}{x}7', 21)
    c = int(f'67564{x}8', 21)
    a = a+b+c
    if a%20==0:
        print(a//20)
        break
#72450445
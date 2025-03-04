from string import *
al = '0123456789' + ascii_lowercase
for p in range(16, 37):
    a = int('17496', p)
    b = int('91f83', p)
    c = int('d9543', p)
    abc = a+b+c
    if abc%12==0:
        print(abc//12)
        break
#318836
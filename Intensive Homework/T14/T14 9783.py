from string import *
al = '0123456789' + ascii_lowercase

for x in al[:22]:
    a = int(f'18{x}89957', 22)
    b = int(f'80{x}33', 22)
    c = int(f'521{x}6', 22)
    a = a+b+c
    if a%21==0:
        print(a//21)
        break
#162947670
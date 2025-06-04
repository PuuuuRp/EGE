from string import *
al = '0123456789' + ascii_lowercase

for x in al[:23]:
    a = int(f'7{x}38596', 23)
    b = int(f'14{x}36', 23)
    c = int(f'61{x}7', 23)
    abc = a+b+c
    if abc%22==0:
        print(abc//22)
        break
#47163321
from string import ascii_lowercase
al = '0123456789' + ascii_lowercase
for x in al[:25]:
    a = int(f'a4{x}7f2', 25)
    b = int(f'n{x}g5{x}h', 25)
    c = int(f'74{x}m26', 25)
    abc = a+b+c
    if abc%24==0:
        print(abc//24)
#16751575
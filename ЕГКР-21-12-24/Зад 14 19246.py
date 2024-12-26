from string import ascii_lowercase
al = '0123456789' + ascii_lowercase
for x in al[:25]:
    a = int(f'11353{x}12', 25)
    b = int(f'135{x}21', 25)
    ab = a+b
    if ab%24 == 0:
        print(ab//24)
#266249847
from string import ascii_lowercase
al = '0123456789' + ascii_lowercase

for x in al[:22]:
    a = int(f'a23{x}ac0', 22)
    b = int(f'gb{x}21670', 22)
    ab = a+b
    if ab%21==0: print(ab//22)
#1923296823
from string import ascii_lowercase
al = '0123456789' + ascii_lowercase

def m_c(abc):
    m = 0
    c = 0
    for i in '0123456789':
        if abc.count(i) >= c:
            m = int(i)
            c = abc.count(i)
    return m

for x in al[1:35]:
    a = int(f'6{x}qr{x}', 35)
    b = int(f'{x}59sh', 35)
    c = int(f'ph{x}69yw', 35)
    abc = a+b+c
    m = m_c(str(abc))**2
    if abc%m == 0:
        print(abc//m)
#46926015711
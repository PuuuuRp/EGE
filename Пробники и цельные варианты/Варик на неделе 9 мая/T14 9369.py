al = '0123456789abcdef'

res = []
for x in al:
    for y in al:
        a = int(f'27a{x}23', 16)
        b = int(f'8{y}e5d2', 16)
        if (a+b)%5==0:
            res.append(int(x, 16)+int(y, 16))
print(max(res))
#29
from ipaddress import *
for a in range(256):
    net = ip_network(f'217.109.{a}.94/23', 0)
    if all(f'{int(i):032b}'[:16].count('0')<=\
               f'{int(i):032b}'[16:].count('0')\
               for i in net):
        print(a)
#129
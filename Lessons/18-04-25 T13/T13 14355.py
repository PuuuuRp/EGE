from ipaddress import *
ip = ip_address('127.63.67.1')
for m in range(33):
    net = ip_network(f'{ip}/{m}', 0)
    if all(f'{int(i):032b}'[:16].count('1')>=\
           f'{int(i):032b}'[16:].count('1')\
           for i in net):
        print(m-16)
        break
#240
from ipaddress import *
c = 0
for a in range(256):
    net = ip_network(f'246.81.65.{a}/255.255.255.224', 0)
    if all(f'{int(ip):032b}'[16:24].count('0')>\
           f'{int(ip):032b}'[24:].count('0')\
           for ip in list(net)[1:-1]):
        c += 1
print(c)
#32
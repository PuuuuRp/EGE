from ipaddress import *

net = ip_network('192.168.31.80/28', 0)
print(max(f'{int(i):032b}'.count('1') for i in net))
#16
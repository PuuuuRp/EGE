from ipaddress import *
net = ip_network('172.16.168.0/255.255.248.0', 0)
c = 0
for ip in net:
    if f'{int(ip):032b}'.count('1')%5!=0:
        c += 1
print(c)
#1663
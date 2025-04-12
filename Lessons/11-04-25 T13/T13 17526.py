from ipaddress import *
net = ip_network('172.16.128.0/255.255.192.0', 0)
c = 0
for ip in net:
    if f'{int(ip):032b}'.count('1')%2!=0: c += 1
print(c)
#8192
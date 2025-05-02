from ipaddress import *
net = ip_network('11.92.135.56/255.224.0.0', 0)
for i in net.hosts():
    print(i)
#1195255254
#11.95.255.254
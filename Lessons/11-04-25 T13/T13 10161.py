from ipaddress import *
for m in range(33):
    net1 = ip_network(f'211.115.61.154/{m}', 0)
    net2 = ip_network(f'211.115.59.137/{m}', 0)
    if net1 == net2:
        print(net1.netmask)
#248
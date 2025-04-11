from ipaddress import *
for m in range(33):
    net1 = ip_network(f'193.175.175.231/{m}', 0)
    net2 = ip_network(f'193.175.176.118/{m}', 0)
    if net1.network_address != net2.network_address:
        print(net1.netmask)
#240
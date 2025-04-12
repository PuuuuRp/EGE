from ipaddress import *
for m in range(33):
    net1 = ip_network(f'157.127.182.76/{m}', 0)
    net2 = ip_network(f'157.127.190.80/{m}', 0)
    if net1.network_address != net2.network_address:
        print(m)
#21
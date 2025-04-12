from ipaddress import *
c = 0
for m in range(33):
    net1 = ip_network(f'112.117.107.70/{m}', 0)
    net2 = ip_network(f'112.117.121.80/{m}', 0)
    if net1.network_address == net2.network_address:
        print(2**(32-m))
#8192
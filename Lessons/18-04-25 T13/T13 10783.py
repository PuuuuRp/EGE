from ipaddress import *
ip1  = ip_address('121.171.5.70')
ip2  = ip_address('121.171.5.107')
for m in range(32, -1, -1):
    net1 = ip_network(f'{ip1}/{m}', 0)
    net2 = ip_network(f'{ip2}/{m}', 0)
    if net1 == net2:
        print(net1.num_addresses)
        break
#64
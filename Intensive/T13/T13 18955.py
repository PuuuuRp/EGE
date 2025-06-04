from ipaddress import *
ip1 = ip_address('200.154.190.12')
ip2 = ip_address('200.154.184.0')
for n in range(32, -1, -1):
    net1 = ip_network(f'{ip1}/{n}', 0)
    net2 = ip_network(f'{ip2}/{n}', 0)
    if net1 == net2 and \
        ip1 not in [net1.network_address, net1.broadcast_address] and \
        ip2 not in [net2.network_address, net2.broadcast_address]:
        print(n)
        break
#20
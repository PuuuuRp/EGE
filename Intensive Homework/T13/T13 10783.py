from ipaddress import *
ip1 = ip_address('121.171.5.70')
ip2 = ip_address('121.171.5.107')
for n in range(30, -1, -1):
    net1 = ip_network(f'{ip1}/{n}', 0)
    net2 = ip_network(f'{ip2}/{n}', 0)
    if net1 == net2 and \
            ip1 in net1.hosts() and ip2 in net2.hosts():
        print(net1.num_addresses)
        break
#64
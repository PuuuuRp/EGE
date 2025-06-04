from ipaddress import *
ip1 = ip_address('10.96.180.231')
ip2 = ip_address('10.96.140.118')
for n in range(31):
    net1 = ip_network(f'{ip1}/{n}', 0)
    net2 = ip_network(f'{ip2}/{n}', 0)
    if net1 != net2 and \
        ip1 in net1.hosts() and ip2 in net2.hosts():
        print(32-n)
        break
#13
from ipaddress import *
ip1 = ip_address('151.172.115.121')
ip2 = ip_address('151.172.115.156')
for m in range(33):
    net1 = ip_network(f'{ip1}/{m}', 0)
    net2 = ip_network(f'{ip2}/{m}', 0)
    if net1 != net2:
        print(m)
        break
#25
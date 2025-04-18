from ipaddress import *
ad = ip_address('111.81.192.0')
for m in range(33):
    net = ip_network(f'111.81.208.27/{m}', 0)
    if ad == net.network_address:
        print(net.netmask)
        break
#192
from ipaddress import *

ad = ip_address('153.202.16.32')
for m in range(32, -1, -1):
    net = ip_network(f'153.202.16.37/{m}', 0)
    if ad == net.network_address:
        print(m-16 - 8)
        print(net.netmask)
        break
print(255 + 248)
#503
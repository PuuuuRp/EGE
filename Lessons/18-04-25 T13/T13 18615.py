from ipaddress import *

ip = ip_address('143.131.211.37')
for m in range(32, -1, -1):
    net = ip_network(f'{ip}/{m}', 0)
    if ip not in [net.network_address,net.broadcast_address]:
        if sum(f'{int(i):032b}'.count('1')==10 for i in net)>=15:
            print(m)
#17
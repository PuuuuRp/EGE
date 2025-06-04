from ipaddress import *
ip1 = ip_address('95.24.2.9')
ip2= ip_address('95.24.3.10')
m = 0
for n in range(33):
    net1 = ip_network(f'{ip1}/{n}', 0)
    net2 = ip_network(f'{ip2}/{n}', 0)
    if net1 != net2 and \
        ip1 not in [net1.network_address, net1.broadcast_address] and \
        ip2 not in [net2.network_address, net2.broadcast_address]:
        cnt = 0
        for ip in net1.hosts():
            if f'{int(ip):032b}'[-1] == '0': cnt += 1
        m = max(m, cnt)
print(m)
#127

from ipaddress import *
ip1 = ip_address('201.44.240.33')
ip2 = ip_address('201.44.240.107')
cnt = 0
for n in range(31):
    net1 = ip_network(f'{ip1}/{n}', 0)
    net2 = ip_network(f'{ip2}/{n}', 0)
    if net1 == net2:
        if f'{int(net1.network_address):032b}'.count('1') >= 5 and \
                ip1 in net1.hosts() and ip2 in net2.hosts():
            cnt += 1
print(cnt)
#15
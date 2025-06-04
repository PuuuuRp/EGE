from ipaddress import *
for n in range(17, 25):
    ip = ip_address('99.8.254.232')
    net = ip_network(f'{ip}/{n}', 0)
    if ip in net.hosts() and \
        all(f'{int(i):032b}'[:16].count('1')<=\
            f'{int(i):032b}'[16:].count('1') for i in net):
        print(n-16)
        break
#248
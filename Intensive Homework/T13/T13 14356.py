from ipaddress import *
for A in range(255):
    ip = ip_address(f'217.109.{A}.94')
    net = ip_network(f'{ip}/255.255.254.0', 0)
    if ip in net.hosts() and \
        all(f'{int(i):032b}'[:16].count('0')<=f'{int(i):032b}'[16:].count('0')\
            for i in net):
        print(A)
#129
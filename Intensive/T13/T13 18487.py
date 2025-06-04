from ipaddress import *
for A in range(256):
    ip = ip_address(f'192.214.{A}.184')
    net = ip_network(f'{ip}/255.255.255.224', 0)
    if ip not in [net.network_address, net.broadcast_address] and \
        all(f'{int(i):032b}'.count('1') > 15 for i in net):
        print(A)
        break
#127
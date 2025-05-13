from ipaddress import *

for a in range(256):
    ip = ip_address(f'183.192.{a}.0')
    net = ip_network(f'{ip}/22', 0)
    if ip not in net.hosts():
        if all(f'{int(i):032b}'[16:].count('1')>3 for i in net):
            print(a)
            break
#60
from ipaddress import *
for A in range(0, 256):
    net = ip_network(f'223.167.{A}.167/255.255.255.192', 0)
    if all(f'{int(ip):032b}'[:16].count('0')<=\
           f'{int(ip):032b}'[16:].count('0') for ip in net):
        print(A)
#248
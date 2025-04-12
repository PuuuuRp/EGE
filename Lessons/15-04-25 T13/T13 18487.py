from ipaddress import *

for A in range(256):
    net = ip_network(f'192.214.{A}.184/255.255.255.224', 0)
    if all(f'{int(ip):032b}'.count('1')>15 for ip in net):
        print(A)
        break
#127
from ipaddress import *

for A in range(33):
    net = ip_network(f'127.63.67.1/{A}', 0)
    if all(f'{int(ip):032b}'[:16].count('1')>=\
           f'{int(ip):032b}'[16:].count('1') \
           for ip in net):
        print(A-16)
        break
print(128 + 64 + 32 + 16)
#240
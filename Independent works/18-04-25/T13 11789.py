from ipaddress import *

for m in range(33):
    net = ip_network(f'99.8.254.232/{m}', 0)
    if all(f'{int(ip):032b}'[:16].count('1') <= f'{int(ip):032b}'[16:].count('1')\
           for ip in net):
        print(m-16)
        break
print(128 + 64 + 32 + 16 + 8)
#248
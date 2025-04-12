from ipaddress import *
for m in range(16, 25):
    net = ip_network(f'246.51.128.202/{m}', 0)
    if all(f'{int(ip):032b}'[:16].count('0')<=\
           f'{int(ip):032b}'[16:].count('0') for ip in net):
        print(m)
        break
print(128 + 64 + 32 + 16 + 8 + 4 + 2)
#254
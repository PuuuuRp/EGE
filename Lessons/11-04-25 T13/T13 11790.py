from ipaddress import *
for mask in range(16, 25):
    net = ip_network(f'152.65.245.132/{mask}', 0)
    if all(f'{int(ip):032b}'[:16].count('0')>=\
           f'{int(ip):032b}'[16:].count('0') for ip in net):
        print(mask)
        break
print(128 + 64 + 32 + 16 + 8 + 4)
#252
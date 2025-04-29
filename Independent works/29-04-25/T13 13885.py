from ipaddress import *
ip = ip_address('238.51.1.202')
for m in range(30, 16, -1):
    net = ip_network(f'{ip}/{m}', 0)
    if ip not in [net.network_address, net.broadcast_address]\
        and all(f'{int(i):032b}'[:16].count('1')>=\
                f'{int(i):032b}'[16:].count('1') for i in net):
        print(m)
print(128 + 64 + 32 + 16 + 8 + 4)
#252
from ipaddress import *
ip = ip_address('156.132.15.138')
net = ip_network(f'{ip}/22', 0)
for pos,i in enumerate(net, 0):
    if ip == i:
        print(pos)
        break
#906
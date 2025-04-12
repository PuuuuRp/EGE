from ipaddress import *
c = 0
for A in range(256):
    net = ip_network(f'207.0.{A}.167/255.255.255.192', 0)
    if all(f'{int(ip):032b}'[:16].count('0')>\
            f'{int(ip):032b}'[16:].count('0') for ip in net):
        c += 1
print(c)
#37
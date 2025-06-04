from ipaddress import *
cnt = 0
for A in range(255):
    ip = ip_address(f'246.81.65.{A}')
    net = ip_network(f'{ip}/255.255.255.224', 0)
    if ip in net.hosts() and\
        all(f'{int(i):032b}'[16:24].count('0')>\
            f'{int(i):032b}'[24:].count('0') for i in net.hosts()):
        cnt += 1
print(cnt)
#120
from ipaddress import *
net = ip_network('112.160.0.0/255.240.0.0', 0)
cnt = 0
for ip in net:
    if f'{int(ip):032b}'.count('1')%5==0:
        cnt += 1
print(cnt)
#215766
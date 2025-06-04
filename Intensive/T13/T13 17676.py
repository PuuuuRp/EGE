from ipaddress import *
net = ip_network('115.192.0.0/255.192.0.0', 0)
cnt = 0
for ip in net:
    if f'{int(ip):032b}'.count('1')%3!=0:
        cnt += 1
print(cnt)
#2796202
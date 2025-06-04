from ipaddress import *
cnt = 0
for ip in ip_network('192.168.32.48/255.255.255.240', 0):
    if f'{int(ip):032b}'.count('1')%2!=0:
        cnt += 1
print(cnt)
#8
from ipaddress import *
cnt = 0
for ip in ip_network('172.16.168.0/255.255.248.0',0):
    if f'{int(ip):032b}'.count('1')%5!=0:
        cnt += 1
print(cnt)
#1663
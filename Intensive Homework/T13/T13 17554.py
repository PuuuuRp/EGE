from ipaddress import *
cnt = 0
for ip in ip_network('112.160.0.0/255.240.0.0', 0):
    if f'{int(ip):032b}'.count('1')%3!=0:
        cnt += 1
print(cnt)
#699050
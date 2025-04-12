from ipaddress import *

ip = ip_address('218.48.192.0')
cnt = 0
for m in range(16, 25):
    net = ip_network(f'218.48.192.56/{m}', 0)
    if net.num_addresses>=500:
       if ip == net.network_address:
           cnt += 1
print(cnt)
#6
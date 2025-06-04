from ipaddress import *
print(*ip_network('11.92.135.56/255.224.0.0', 0).hosts())
#11.95.255.254
#1195255254
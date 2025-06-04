from ipaddress import *
print(max(ip_network('143.168.72.213/255.255.255.240', 0).hosts()))
#143.168.72.222
#14316872222
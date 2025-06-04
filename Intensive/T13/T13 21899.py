from ipaddress import *
print(*ip_network('98.81.154.195/255.252.0.0', 0).hosts())
#98.83.255.254
#9883255254
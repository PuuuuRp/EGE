from ipaddress import *
print(max(ip_network('218.194.82.148/255.255.255.192', 0).hosts()))
#218.194.82.190
#21819482190
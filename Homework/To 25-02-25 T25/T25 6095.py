from fnmatch import *
for i in range(10**8):
    u1 = i%111==0 and i%113!=0 and i%127!=0
    u2 = i%111!=0 and i%113==0 and i%127!=0
    u3 = i%111!=0 and i%113!=0 and i%127==0
    if fnmatch(str(i), '*15*7424') and (u1 or u2 or u3):
        if i%111==0: print(i, i//111)
        elif i%113==0: print(i, i//113)
        elif i%127==0: print(i, i//127)

# 1587424 14048
# 15147424 134048
# 15227424 137184
# 15457424 121712
# 28157424 221712
# 85157424 767184
from itertools import *
al = 'КИДАЛА'
res = []
for val in permutations(al, 5):
    val = ''.join(val)
    if val not in res and 'АА' not in val:
        res.append(val)
print(len(res))
#264
from itertools import *
al = 'МАКАКА'
res = []
for val in permutations(al, 6):
    val = ''.join(val)
    if val not in res and all(i*2 not in val for i in al):
        res.append(val)
print(len(res))
#10
from itertools import *
al = 'соточка'
gl = [''.join(i) for i in set(permutations('ооа',2))]
c = 0
for val in set(permutations(al)):
    val = ''.join(val)
    if any(i in val for i in gl): c+=1
print(c)
#1800
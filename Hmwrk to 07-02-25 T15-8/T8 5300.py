from itertools import *
al = 'хочу*в*вуз.'
c = 0
for val in set(permutations(al)):
    val = ''.join(val)
    if '*у' not in val and val[0] not in '*у' \
            and val[-1] == '.' and val[-2] != '*'\
            and '**' not in val:
        c += 1
print(c-1) #т.к. по условию она составляет НОВЫЕ слова, а исходное НЕНОВОЕ
#75599
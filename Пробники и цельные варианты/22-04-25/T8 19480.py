from itertools import *
al = 'парижанка'
cnt = 0
for val in set(permutations(al)):
    val = ''.join(val)
    if all(''.join(i) not in val for i in permutations('иааа', 3)) and \
            (('аа' in val and 'аи' not in val and 'иа' not in val) or \
            ('аа' not in val and 'аи' not in val and 'иа' in val) or \
            ('аа' not in val and 'аи' in val and 'иа' not in val)):
        cnt += 1
print(cnt)
#28800
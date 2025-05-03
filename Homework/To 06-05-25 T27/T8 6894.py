from itertools import *
al = 'алпця'

for pos, val in enumerate(product(al, repeat=5), 1):
    val = ''.join(val)
    if val.count('а')<=1 and val.count('ц')==2 and 'л' not in val:
        print(pos)
        break
#319
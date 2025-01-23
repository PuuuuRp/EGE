from itertools import *
with open('24_8510.txt') as f:
    st = f.readline()

for val in product('NOP', repeat=2):
    val = ''.join(val)
    st = st.replace(val, 'P P')
st = st.split()
print(len(max(st, key=len)))
#57
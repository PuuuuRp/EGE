from itertools import *
with open('24_7600.txt') as f:
    st = f.readline()

for i in range(2):
    for val in product('QRS', repeat=2):
        val = ''.join(val)
        st = st.replace(val, val[0] + ' ' + val[1])
st = st.split()

print(max(st, key=len))
print(len(max(st, key=len)))
#544
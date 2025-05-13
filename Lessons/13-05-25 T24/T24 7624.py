from itertools import *
with open('24_7624.txt') as f:
    st = f.readline()

for i in range(2):
    for val in product('XYZ', repeat=2):
        val = ''.join(val)
        st = st.replace(val, 'X X')
st = st.split()

print(max(st, key=len))
print(len(max(st, key=len)))
#786
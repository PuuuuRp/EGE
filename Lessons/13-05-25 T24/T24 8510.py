from itertools import *
with open('24_8510.txt') as f:
    st = f.readline()
st = st.replace('O', 'N').replace('P', 'N')
for i in range(2):
    st = st.replace('NN', 'N N')
st = st.split()

print(max(st, key=len))
print(len(max(st, key=len)))
#57
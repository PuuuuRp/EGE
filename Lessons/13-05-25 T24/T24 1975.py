with open('24_1975.txt') as f:
    st = f.readline()

for i in range(2): st = st.replace('PP', 'P P')
st = st.split()

print(len(max(st, key=len)))
#188
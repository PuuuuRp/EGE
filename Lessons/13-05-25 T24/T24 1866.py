with open('24_1866 (1).txt') as f:
    st = f.readline()

for i in range(2):
    st = st.replace('ad', 'a d')
    st = st.replace('da', 'd a')
st = st.split()

print(len(max(st, key=len)))
#2252
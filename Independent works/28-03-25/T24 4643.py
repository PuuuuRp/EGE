with open('24_4643.txt') as f:
    st = f.readline()
st = st.replace('B', 'A').replace('2', '1')
st = st.replace('AA', 'A ')
st = st.replace('A1A', 'A')
while ' A' in st or '1 ' in st or '111' in st:
    st = st.replace(' A', ' ')
    st = st.replace('1 ', ' ')
    st = st.replace('111', ' 11')
st = st.split()
print(len(max(st, key=len))//3)
#67

with open('24_4643.txt') as f:
    st = f.readline()
st = st.replace('B', 'A').replace('2', '1')
st = st.replace('11A', '*')
st = st.replace('A', ' ')
st = st.replace('1', ' ')
st = st.split()
print(len(max(st, key=len)))
#67
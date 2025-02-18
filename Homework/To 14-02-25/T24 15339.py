with open('24_15339.txt') as f:
    st = f.readline()
st = st.replace('B', 'A').replace('C', 'A')
st = st.replace('8', '6').replace('7', '6').replace('9', '6')

st = st.replace('AA', 'A A').replace('66', '6 6')
st = st.replace('AA', 'A A').replace('66', '6 6')
st = st.split()

print(len(max(st, key=len)))
#22
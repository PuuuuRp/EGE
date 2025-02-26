with open('24_17756.txt') as f:
    st = f.readline()
st = st.replace('**', '* *')
st = st.replace('++', '* *')
st = st.replace('*+', '* *')
st = st.replace('+*', '* *')

st = st.split()
print(max(st, key=len))
print(len(max(st, key=len)))
#191
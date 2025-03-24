with open('2418.txt') as f:
    st = f.readline()
st = st.replace('++', ' ').replace('**', ' ').replace('+*', ' ').replace('*+', ' ')
st = st.replace(' +', ' ').replace(' *', ' ').replace('* ', ' ').replace('+ ', ' ')

for i in '13579':
    while i+'*' in st or i+'+' in st:
        st = st.replace(i+'+', ' ')
        st = st.replace(i+'*', ' ')

st = st.split()

print(max(st, key=len))
print(len(max(st, key=len)))
#127
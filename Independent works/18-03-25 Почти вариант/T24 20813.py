with open('24_20813.txt') as f:
    st = f.readline()

st = st.replace('8', '7').replace('9', '7')
st = st.replace('**', ' ').replace('--', ' -').replace('*-', ' -').replace('-*', ' ')
st = st.replace('* ', ' ').replace(' *', ' ').replace('- ', ' ').replace(' -', ' ')

while ' 00' in st or '*00' in st or '-00' in st:
    st = st.replace(' 00', ' 0')
    st = st.replace('*00', '*0 0')
    st = st.replace('-00', '-0 0')

while ' 07' in st or '*07' in st or '-07' in st:
    st = st.replace(' 07', ' 7')
    st = st.replace('*07', '*0 7')
    st = st.replace('-07', '-0 7')

st = st.split()

print(len(max(st, key=len)))
print(max(st, key=len))
#111
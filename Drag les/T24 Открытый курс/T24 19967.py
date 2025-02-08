with open('24_19967.txt') as f:
    st = f.readline()

mistakes = ['**', '++', 'B', 'C', 'E', 'D0']
for i in mistakes:
    while i in st:
        st = st.replace(i, ' ')

for i in '0123456789':
    st = st.replace(i+'AFD', '1 AFD')

for i in '0123456789':
    st = st.replace('+0'+i, '+0 1')
    st = st.replace('*0'+i, '*0 1')
    st = st.replace(' 0'+i, ' 1')
st = st.split()

res = []
for i in st:
    if 'AFD' in i:
        res.append(i)
print(max(res, key=len), len(max(res, key=len)))
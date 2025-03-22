with open('24_105.txt') as f:
    st = f.readline()
for x in 'FAIL':
    for y in 'FAIL':
        if x!=y:
            st = st.replace(x+y, x+' '+y)
st = st.split()

print(len(max(st, key=len)))
#75
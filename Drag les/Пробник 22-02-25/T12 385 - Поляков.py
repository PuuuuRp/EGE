c = 0
for n in range(12345, 13457):
    st = n*'1'
    while '111' in st:
        st = st.replace('111', '2', 1)
        st = st.replace('222', '11', 1)
        st = st.replace('1', '2', 1)
    if '1' not in st:
        c += 1
print(c)
#210
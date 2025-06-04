for n in range(4, 10000):
    st = '4' + '2'*n
    while '42' in st or '2222' in st or '8222' in st:
        st = st.replace('42', '2', 1)
        st = st.replace('8222', '24', 1)
        st = st.replace('2222', '8', 1)
    if sum(int(i) for i in st)==110:
        print(n)
        break
#1591
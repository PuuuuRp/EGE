for n in range(101, 10000):
    st = n*'5'
    while '555' in st or '11' in st or '2' in st:
        st = st.replace('555', '1', 1)
        st = st.replace('11', '25', 1)
        st = st.replace('2', '5', 1)
    if st == '15':
        print(n)
        break
#104
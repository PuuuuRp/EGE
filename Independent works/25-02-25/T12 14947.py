res = []
for n in range(4, 10000):
    st = '1'+n*'9'
    while '19' in st or '49' in st or '999' in st:
        st = st.replace('19', '9', 1)
        st = st.replace('49', '91', 1)
        st = st.replace('999', '4', 1)
    res.append(sum(int(i) for i in st))
print(max(res))
#23
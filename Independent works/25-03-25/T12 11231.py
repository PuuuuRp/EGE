res = []
for n in range(4, 2000):
    st = n*'3' + '5'
    while '23' in st or '5333' in st or '33333' in st:
        st = st.replace('23', '3', 1)
        st = st.replace('5333', '32', 1)
        st = st.replace('33333', '55', 1)
    res.append(sum(int(i) for i in st))
print(min(res))
#10
st = '1' + 90*'0'
while '1' in st:
    if '10' in st:
        st = st.replace('10', '0001', 1)
    else:
        st = st.replace('1', '000', 1)
print(len(st))
#273
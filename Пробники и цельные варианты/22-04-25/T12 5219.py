cnt = 0
for n in range(1, 101):
    st = '1' + n*'0'
    while '10' in st or '1' in st:
        if '10' in st:
            st = st.replace('10', '0001', 1)
        else:
            st = st.replace('1', '0', 1)
    if len(st)%7==0: cnt += 1
print(cnt)
#15
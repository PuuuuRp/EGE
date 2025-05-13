for n in range(1, 100):
    for x in range(1, 100):
        for y in range(1, 100):
            st = '0' + n*'1' + x*'2' + y*'3'
            while '01' in st or '02' in st or '03' in st:
                st = st.replace('01', '30', 1)
                st = st.replace('02', '3103', 1)
                st = st.replace('03', '1201', 1)
            if st.count('1') == 31 and st.count('2') == 24 and st.count('3') == 46:
                print(y)
#17
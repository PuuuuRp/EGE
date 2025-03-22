with open('24_4682.txt') as f:
    st = f.readline()
st = st.replace('C', 'B').replace('D', 'B').replace('A', 'E')
st = st.replace('BB', 'B B').replace('EE', 'E E')
st = st.replace(' BE', ' E').replace('BE ', 'B ')
st = st.split()

print(len(max(st, key=len))//2)
#202
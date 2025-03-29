with open('24_5237.txt') as f:
    st = f.readline()
st = st.replace('Z', ' ')
st = st.replace('XX', 'X X').replace('YY', 'Y Y')
st = st.replace('XX', 'X X').replace('YY', 'Y Y')
st = st.split()

print(max(st, key=len))
print(len(max(st, key=len)))
#15
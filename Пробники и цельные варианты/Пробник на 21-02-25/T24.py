with open('24.txt') as f:
    st = f.readline()

st = st.replace('SS', 'S S')
st = st.replace('SS', 'S S')
st = st.replace('QS', 'Q S').replace('SR', 'S R')
st = st.replace('QS', 'Q S').replace('SR', 'S R')

st = st.split()

print(max(st))
print(len(max(st)))
#51
with open('24_4544.txt') as f:
    st = f.readline()
st = st.replace('XIX', 'XI IX').split()

print(max(st, key=len))
print(len(max(st, key=len)))
#293
with open('24_2421.txt') as f:
    st = f.readline()
st = st.replace('D', ' ').split()

print(max(st, key=len))
print(len(max(st, key=len)))
#44
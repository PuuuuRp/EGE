from string import ascii_uppercase
al = '0123456789' + ascii_uppercase

with open('24_10724.txt') as f:
    st = f.readline()

for i in al[16:]:
    st = st.replace(i, ' ')
for i in range(200, 0, -1):
    st.replace(' '+'0'*i, ' ')
st = st.split()

last = 0
for i in st:
    if last<=len(i):
        print(i)
        print(len(i))
        last = len(i)
#21
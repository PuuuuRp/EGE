st = '>'+'3'*10+'5'*10+10*'7'
while '>3' in st or '>5' in st or '>7' in st:
    st = st.replace('>3', '55>')
    st = st.replace('>5', '5>3')
    st = st.replace('>7', '3>5')
print(sum(int(i) for i in st[:-1]))
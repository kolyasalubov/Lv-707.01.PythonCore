st = str(input('please enter your string: '))
def reverse(st):
    l = st.split()
    l = l[::-1]
    st = ' '.join(str(a) for a in l)
    return st
print(reverse(st))
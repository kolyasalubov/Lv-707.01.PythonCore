def filter_words(st: str) -> str:
    st = st.capitalize().strip()
    while st.count('  ') > 0:
        st = st.replace('  ', ' ')
    return st

print(filter_words("This    will    not    pass "))
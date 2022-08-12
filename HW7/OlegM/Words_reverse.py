def reverse(st: str) -> str:
    ''' reverses the words'''
    st = " ".join(st.split()[::-1])
    return st


print(reverse("Hallo Python !"))

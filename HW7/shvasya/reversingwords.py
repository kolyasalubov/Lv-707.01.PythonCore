def reverse(st):
    # Your Code Here
    words = st.split()
    revwords = list(reversed(words))
    newwords = ' '.join(revwords)
    return newwords

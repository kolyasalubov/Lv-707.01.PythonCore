def filter_words(st):
    l = st.split()
    l = [a.lower() for a in l]
    l = ' '.join(a for a in l)
    l.capitalize()
    return(l.capitalize())
print(filter_words(st = 'EWGWgwegewgewgewwe 2eefwegwgg42g2     WEGWGGGEWGEWgewwefwefw 3fe3wffewgewge'))
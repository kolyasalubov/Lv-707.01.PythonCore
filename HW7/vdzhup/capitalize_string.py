def filter_words(st):
    capitalize_str = st.capitalize()
    return " ".join(capitalize_str.split())


print(filter_words("HELLO CAN YOU     HEAR ME"))

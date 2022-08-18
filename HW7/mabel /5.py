def filter_words(stroka):
    stroka_str = stroka.capitalize()
    return " ".join(stroka_str.split())


print(filter_words("HELLO CAN YOU     HEAR ME"))
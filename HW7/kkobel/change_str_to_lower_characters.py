def filter_words(string):
    change_to_capitalize_str = " ".join(string.split()).capitalize()
    return change_to_capitalize_str

print(filter_words("CAN    YOU     HEAR     ME"))

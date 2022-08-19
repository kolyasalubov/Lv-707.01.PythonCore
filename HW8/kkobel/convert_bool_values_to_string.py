'''
Convert boolean values to strings 'Yes' or 'No'.
'''

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

print(bool_to_word(2+2))
print(bool_to_word(True))
print(bool_to_word(12 > 0))
print(bool_to_word(False))
print(bool_to_word(0))
print(bool_to_word(""))

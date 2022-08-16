def calculates_number_characters(word):
    unique_characters = dict.fromkeys(word, 0)

    for item in word:
        unique_characters[item] += 1
    return unique_characters


print(calculates_number_characters("hello"))

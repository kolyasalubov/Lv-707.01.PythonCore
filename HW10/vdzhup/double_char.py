def double_char(s: str) -> str:
    new_word = ""

    for item in s:
        new_word += item * 2
    return new_word

print(double_char("String"))

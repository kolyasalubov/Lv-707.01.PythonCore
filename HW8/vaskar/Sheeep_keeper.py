from html.entities import codepoint2name


f = [True, False, False, True, True, True]
def count_sheeps(sheep):
    return sheep.count(True)

print(count_sheeps(f))
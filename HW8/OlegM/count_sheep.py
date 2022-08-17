def count_sheeps(sheep: list) -> int:
    # count true in list
    return sheep.count(True)

print(count_sheeps([True, True, True, True, True, True, True, False]))
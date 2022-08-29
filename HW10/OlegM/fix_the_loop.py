def list_animals(animals: list) -> str:
    return "".join([str(i) + '. ' + animal + '\n' for i, animal in enumerate(animals, 1)])


animals = ['dog', 'cat', 'elephant']
print(list_animals(animals))

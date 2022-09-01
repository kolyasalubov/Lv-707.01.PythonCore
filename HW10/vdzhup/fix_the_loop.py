def list_animals(animals: list) -> str:
    my_list = ""
    for i in animals:
        my_list += str(animals.index(i)) + ". " + i + "\n" 
    return my_list


print(list_animals([ "dog", "cat", "elephant" ]))

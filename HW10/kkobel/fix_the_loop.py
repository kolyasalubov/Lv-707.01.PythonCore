def list_animals(animals):
    list = ''
    for element in range(len(animals)):
        list += str(element + 1) + '. ' + animals[element] + '\n'
    return list

print(f"Result of list animals: \n{list_animals([ 'dog', 'cat', 'elephant' ])}") 

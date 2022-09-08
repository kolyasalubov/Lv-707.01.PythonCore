def list_animals(animals):
    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list

animals = ['cat', 'dog','bat', 'rat','fox']
print(list_animals(animals))
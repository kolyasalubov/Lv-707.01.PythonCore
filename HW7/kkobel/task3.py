def count_numbers_in_string(string):
    '''
    Function that calculates the number of characters
    '''
    change_to_enumerate = enumerate(string)
    change_to_dict = dict(change_to_enumerate)
    list_of_dictionary = {}
    for val in change_to_dict.values():
        count_of_value = string.count(val)
        list_of_dictionary.update({val: count_of_value})
    print(f"Your count of elements: {list_of_dictionary}") 
user_input_string = count_numbers_in_string(input("Enter your string: "))

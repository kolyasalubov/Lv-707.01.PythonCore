def count_numbers_in_string(string):
    '''
    Function that calculates the number of characters
    '''
    result_of_dictionary = {}
    for element in string:
        if element in result_of_dictionary:
            continue
        else:
            result_of_dictionary.update({str(element): string.count(element)})
    return result_of_dictionary   

print("Your count of string is:", count_numbers_in_string('Good days'))
print("Your count of string is:", count_numbers_in_string('1005500'))
print("Your count of string is:", count_numbers_in_string('$sabkjdnl'))
print("Your count of input string is:", count_numbers_in_string(input("Enter your string: "))) 

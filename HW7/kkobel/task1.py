def return_the_largest_number_of_two_numbers(number1: int,number2: int):
    ''' 
    Function that returns 
    the largest number of two
    numbers
    '''
    if number1 > number2:
        return number1
    elif number2 > number1:
        return number2
    elif number1 == number2:
        print(f"Number1: {number1} is equal Number2: {number2}")

result_of_two_equals_numbers = return_the_largest_number_of_two_numbers(12,12)
first_result_of_two_numbers = print(f"Number1 is the largest than Number2 and equal:",return_the_largest_number_of_two_numbers(12,10))
second_result_of_two_numbers = print(f"Number2 is the largest than Number1 and equal:",return_the_largest_number_of_two_numbers(100,1000))
print(return_the_largest_number_of_two_numbers.__doc__)

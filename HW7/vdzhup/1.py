def get_largest_number(first_number, second_number):
    """
    This function returns the largest number
    of two numbers
    """
    if first_number > second_number:
        return f"{first_number} is largest than {second_number}"
    elif first_number < second_number:
        return f"{second_number} is largest than the {first_number}"
    else:
        return f"{first_number} and {second_number} are equal"


input_first_number = int(input("Enter the first number: "))
input_second_number = int(input("Enter the second number: "))

print(get_largest_number(input_first_number, input_second_number))

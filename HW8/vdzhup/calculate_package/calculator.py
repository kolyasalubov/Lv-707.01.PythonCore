def number_sum():
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    return "Sum of numbers = {}".format(first_number + second_number)

def number_difference():
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    return first_number - second_number

def number_product():
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    return first_number * second_number

def number_division():
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    try:
        return first_number / second_number
    except ZeroDivisionError:
        return "Division by zero is not possible"

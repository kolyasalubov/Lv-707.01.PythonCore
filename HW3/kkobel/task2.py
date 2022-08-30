#First part of Task

four_digit_natural_number = input('Enter four digit natural number: ')
change_to_list_of_numbers = list(four_digit_natural_number)
print(change_to_list_of_numbers)

multiplication_of_numbers = (int(change_to_list_of_numbers[0]) * int(change_to_list_of_numbers[1]) * int(change_to_list_of_numbers[2]) *
int(change_to_list_of_numbers[3]))

print(f"Product of a four-digit number is: {multiplication_of_numbers}")

# Second part of Task

four_integer_natural_number = int(input("Enter four digit natural number: "))
reversed__of_number = 0

while four_integer_natural_number != 0:  
    digit_of_number = four_integer_natural_number % 10
    reversed__of_number = reversed__of_number * 10 + digit_of_number
    four_integer_natural_number //= 10
print(f"Reversed number is: {reversed__of_number}")    

# Third part of Task

change_to_list_of_string = str(reversed__of_number)
sort_list_of_number = sorted(change_to_list_of_string)
print(f"Sort of numbers is : {sort_list_of_number}")  

user_input = int(input("Enter count of numbers: "))

list_of_integer_numbers = [(int(input("Enter your number: "))) for number in range(user_input) ]

print(f"List of integer numbers are: {list_of_integer_numbers}")

list_of_float_numbers = []
for element in list_of_integer_numbers:
    list_of_float_numbers.append(float(element))

print(f"List of float numbers are: {list_of_float_numbers}")

count = 0
while count < 5:
    if count == 0:
        list_of_float_numbers.append(float(list_of_integer_numbers[0]))
    elif count == 1:
        list_of_float_numbers.append(float(list_of_integer_numbers[1]))
    elif count == 2:
        list_of_float_numbers.append(float(list_of_integer_numbers[2]))
    elif count == 3:
        list_of_float_numbers.append(float(list_of_integer_numbers[3]))
    elif count == 4:
        list_of_float_numbers.append(float(list_of_integer_numbers[4]))             
    count += 1
    
print(f"List of float numbers are: {list_of_float_numbers}")

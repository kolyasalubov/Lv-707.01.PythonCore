factorial_of_number = int(input('Enter number of factorial: '))
factorial_n = 1

list_of_factorial = []
if factorial_of_number == 0 or factorial_of_number == 1:
    print(f"Factorial of number is: {factorial_of_number}")
elif factorial_of_number < 0:
    print(f"Factorial {factorial_of_number} isn't positive and can't be exist")
else:
    for element in range(1,factorial_of_number+1):
        factorial_n *= element
        print(factorial_n)
        list_of_factorial.append(factorial_n)
    print(list_of_factorial)
    print(f"Factorial of number {factorial_of_number} is: {factorial_n}")

count = 1

if factorial_of_number == 0 or factorial_of_number == 1:
    print(f"Factorial of number is: {factorial_of_number}")
elif factorial_of_number < 0:
    print(f"Factorial {factorial_of_number} isn't positive and can't be exist")
else:
    while count < factorial_of_number+1:
        factorial_n *= count
        print(factorial_n)
        count += 1
        list_of_factorial.append(factorial_n)
    print(list_of_factorial)
    print(f"Factorial of number {factorial_of_number} is: {factorial_n}")

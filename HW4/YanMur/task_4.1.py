# Task 1
number = int(input("Enter factorial number: "))

counter = 1
factorial = 1

if number == 1 or number == 0:
    factorial = 1
    print(f"{number}! = {factorial}")
elif number < 0:
    print(f"No factorial for this number.")
else:
    while counter <= number:
        factorial = factorial * counter
        counter +=1
    print(f"{number}! = {factorial}")
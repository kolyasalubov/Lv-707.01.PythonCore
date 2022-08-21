# Task 2

number = input("Enter four digit number:\n")

multiplication = 1
digits_list = list(str(number))

for digit in digits_list:
    multiplication *= int(digit)

print(f"Digit multiplication of number {number} is {multiplication}")
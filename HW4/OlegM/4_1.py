'''Write a script that will calculate
the factorial of the entered number
without using recursion.'''


values: int = int(input("Enter number for calculate the factorial:"))
result: float = 1
if values < 0:
    print(f"Factorial of: {values} not exist, {values} is negative number")
elif values == 0 or values == 1:
    print(f"Factorial of {values} = {result}")
elif values > 1:
    for i in range(1, values+1):
        result *= i
    print(f"Factorial of {values} = {result}")
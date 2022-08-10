'''Write a script that will calculate
the factorial of the entered number
without using recursion.'''


values: int = int(input("Enter number for calculate the factorial:"))
result: float = 1
for i in range(1, values+1):
    result *= i
print(f"Factorial of {values} = {result}")
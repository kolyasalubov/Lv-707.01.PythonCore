##### first way (using "while") #######

user_factorial = int(input("Enter only the positive number for the factorial: "))

factorial_count = 1

if user_factorial == 1 or user_factorial == 0:
    print(f"The factorial of the number {user_factorial}! is: {factorial_count}")
elif user_factorial < 0:
    print(f"{user_factorial} is non positive number!")
else:
    while user_factorial > 1:
        factorial_count *= user_factorial
        user_factorial -= 1
    print(f"The factorial of the number {user_factorial}! is: {factorial_count}")



##### second way (using "for") #########

user__factorial = int(input("Enter only the positive number for the factorial: "))

factorial__count = 1

if user__factorial == 1 or user__factorial == 0:
    print(f"The factorial of the number {user__factorial}! is: {factorial__count}")
elif user__factorial < 0:
    print(f"{user__factorial} is non positive number!")   
else:
    for i in range(1, user__factorial + 1):
        factorial__count *= i
    print(f"The factorial of the number {user__factorial}! is: {factorial__count}")

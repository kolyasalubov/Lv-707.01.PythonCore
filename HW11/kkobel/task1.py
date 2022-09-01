'''
Write a program that prompts the user to enter their age, and then displays a
message stating whether the age is even or odd. The program must provide the ability
to enter a negative number, and in this case generate an exception. The master code
should call a function that processes the information entered.
'''

user_input = int(input('Enter your age: '))
try:
    if user_input < 0:
        raise ValueError("Your age is not a positive")   
    elif user_input %2 == 0:
        print(f"Your age is {user_input} and it's even age")
    else:
        print(f"Your age is {user_input} and it's odd age")
          
except ValueError as e:
    print(f"{e}")

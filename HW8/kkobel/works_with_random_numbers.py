from random import randint


result_of_random = randint(1,100)
user_input = int(input('Enter integer number: '))
while True:
    if user_input == result_of_random:
        print(f"Your number is: {user_input}")
        print('Congratilations you win your prize!!!')
        break
    elif user_input > result_of_random:    
        print(f"Your number {user_input} is bigger than Our Random Number")
        user_input = int(input('Enter integer number: '))
    elif user_input < result_of_random:
        print(f"Your number {user_input} is less than Our Random Number")
        user_input = int(input('Enter integer number: '))

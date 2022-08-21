import random

random_number = random.randint(1, 100)

while True:
    user_input_num = int(input("Try to guess the number, enter your number: "))
    if user_input_num == random_number:
        print(f"You guessed the number, it was {random_number}")
        break
    elif user_input_num < random_number:
        print(f"Your number {user_input_num} is less than the number the program has guessed")
    else:
        print(f"Your number {user_input_num} is greater than the number the program has guessed")

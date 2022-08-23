import random
random_number = random.randint(1, 100)
user_input = int(input("Enter your number : "))
while user_input != random_number:
    if user_input > random_number:
        print("Your number is bigger than a random number, you'll get lucky next time")
    elif user_input < random_number:
        print("Your number is smaller than a random number, you'll get lucky next time")
    user_input = int(input("Please try again "))    
else:
    print("Good job")   
from random import randint

random_number = randint(1, 100)
while (number := int(input("Guess a number from 1 to 100: "))) != random_number:
    print("Your number is greater than the origin number" if number > random_number else "Your number is less than "
                                                                                         "the origin number")
else:
    print(f"Bingo! Winner number is {number}!!!")
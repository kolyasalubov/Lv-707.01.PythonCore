from random import randint

def guess_number():
    number=randint(0,999)
    while True:
        answear=int(input("Try to guess the number!"))
        if answear==number:
            print("The number was:", number)
            break
        if answear>number:
            print("Your number is to big")
        elif answear<number:
            print("Your number is to little")
    return number


guess_number()
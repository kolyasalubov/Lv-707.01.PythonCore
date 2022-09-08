import random
hidden = random.randint(1,100)
guess = int(input("guess the number"))
while True:
    if hidden == guess:
        print("you are the lucky one! the number indeed is:", hidden)
        break
    elif hidden > guess:
        print("Larger!")
        guess = int(input("guess the number"))
    else:
        print("Smaller!")
        guess = int(input("guess the number"))
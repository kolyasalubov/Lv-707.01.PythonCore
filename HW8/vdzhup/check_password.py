import re

def validation_password():

    flag = True

    while True:
        user_password = input("Enter your password: ")
        if not (6 <= len(user_password) <= 16):
            flag = False
            print("Password must be between 6 and 16 characters long")
            break
        elif not re.findall("[a-z]", user_password):
            flag = False
            print("You need to use at least 1 letter between [a-z]")
            break
        elif not re.findall("[A-Z]", user_password):
            flag = False
            print("You need to use at least 1 letter between [A-Z]")
            break
        elif not re.findall("[$, #, @]", user_password):
            flag = False
            print("You need to use at least 1 character from [$#@]")
            break
        elif not re.findall("\d", user_password):
            flag = False
            print("You need to use at least 1 number between [0-9]")
            break
        elif len(user_password) > 16 or len(user_password) < 6:
            flag = False
            print("Password must be between 6 and 16 characters long")
            break
        else:
            flag = True
            print("You entered a valid password!")

    if flag == False:
        print("You entered not a valid password")


validation_password()

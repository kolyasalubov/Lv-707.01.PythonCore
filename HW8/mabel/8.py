import re

def passwd():
    tru = True

    password = input("Enter your passwword ")

    while tru:
        if len(password) < 6 or len(password) > 16:
            print("Enter valid password")
            break
        elif not re.search("[a-z]", password):
            print("Enter valid password")
            break
        elif not re.search("[A-Z]", password):
            print("Enter valid password")
            break
        elif not re.search("[0-9]", password):
            print("Enter valid password")
            break
        elif not re.search("[$#@]", password):
            print("Enter valid password")
            break
        else:
            print("Valid Password")
            tru=False
            break
    if tru == False:
        print("Enter valid password")

passwd()

    



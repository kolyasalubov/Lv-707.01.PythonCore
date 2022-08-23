import re

password = input("Enter a password: ")

while True:
    if not re.findall("[a-z]", password):
        print("password is invalid.TRY AGAIN MATCHING ALL THE REQUIREMENTS")
        password = input("Enter a password: ")
    if not re.findall("[0-9]", password):
        print("password is invalid.TRY AGAIN MATCHING ALL THE REQUIREMENTS")
        password = input("Enter a password: ")
    if not re.findall("[A-Z]", password):
        print("password is invalid.TRY AGAIN MATCHING ALL THE REQUIREMENTS")
        password = input("Enter a password: ")
    if not 6 < len(password) < 16:
        print("password is invalid.TRY AGAIN MATCHING ALL THE REQUIREMENTS")
        password = input("Enter a password: ")
    if not re.findall("[$#@]", password):
        print("password is invalid.TRY AGAIN MATCHING ALL THE REQUIREMENTS")
        password = input("Enter a password: ")
    else:
        print("Touche!Correct password")
        break        
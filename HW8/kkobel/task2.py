import re


def check_password(password):
    '''
    Write a Python program to check the validity of a password (input from users).
    Validation :
    At least 1 letter between [a-z] and 1 letter between [A-Z].
    At least 1 number between [0-9].
    At least 1 character from [$#@].
    Minimum length 6 characters.
    Maximum length 16 characters.
    '''
    validate_of_lower_letters = re.findall(("[a-z]") , password)
    validate_of_upper_letters = re.findall(("[A-Z]") , password)
    validate_of_numbers = re.findall(("[0-9]") , password)
    validate_of_symbols = re.findall(("[$#@]") , password)

    flag = True
    while flag:
        if len(password) < 6:
            print('Your password have to have minimum length 6 characters')
            break
        elif len(password) > 16:
            print('Your password have to have maximum length 16 characters')
            break
        elif not validate_of_lower_letters:
            print('Your password have to have least 1 letter between [a-z]')
            break
        elif not validate_of_upper_letters:
            print('Your password have to have least 1 letter between [A-Z]')
            break
        elif not validate_of_numbers:
            print('Your password have to have least 1 number between [0-9]')
            break
        elif not validate_of_symbols:
            print('Your password have to have least 1 character from [$#@]')
            break
        else:
            print(f"Your entered password: {password} is valid")
            flag = False
            break
    if flag:
         return f"Your entered password: {password} is invalid"

check_password(f"{input('Enter you password: ')}")                     

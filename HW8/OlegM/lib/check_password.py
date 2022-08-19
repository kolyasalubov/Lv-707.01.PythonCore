import string
import re


def is_incl_letter_low(passwd: str) -> bool:
    # At least 1 letter between [a-z] and 1 letter between [A-Z].
    # if any([i in string.ascii_uppercase for i in passwd]):
    if len(re.findall('[a-z]', passwd)) != 0:
        return True
    else:
        print(f"Password need include at least 1 letter between [a-z]")
        return False


def is_incl_letter_upper(passwd: str) -> bool:
    # At least 1 letter between [A-Z] and 1 letter between [A-Z].
    # if any([i in string.ascii_uppercase for i in passwd]):
    if len(re.findall('[A-Z]', passwd)) != 0:
        return True
    else:
        print(f"Password need include at least 1 letter between [A-Z]")
        return False


def is_incl_digit(passwd: str) -> bool:
    # At least 1 number between [0-9].
    # if any([str(num) in passwd for num in range(10)]):
    if len(re.findall('[\d]', passwd)) != 0:
        return True
    else:
        print(f"Password need include at least 1 number between [0-9]")
        return False


def is_incl_uniq(passwd: str) -> bool:
    # At least 1 character from [$ # @]
    # if any([i in passwd for i in ['$', '#', '@']]):
    if len(re.findall('[$, @, #]', passwd)) != 0:
        return True
    else:
        print(f"Password need include at least 1 character from [$ # @]")
        return False


def check_lenght(passwd: str) -> bool:
    # Lenght need be >= 6 and <= 16
    if 6 <= len(passwd) <= 16:
        return True
    else:
        print(f"Length of password need be minimum 6 and maximum 16 symbols ")
        return False


LIST_OF_FUNCTION = (is_incl_letter_upper, is_incl_letter_low, is_incl_digit, is_incl_uniq, check_lenght)


# List of check-functions


def correct_passwd(passwd: str, lst_of_function: list) -> bool:
    '''
    :param lst_of_function: list of check-function
    :param passwd:  password
    :return: result of check-functions
    '''
    return all([func(passwd) for func in lst_of_function])


def correct_passwd_short(passwd: str, lst_of_function: list) -> bool:
    '''
    break after fierst False result
    :param lst_of_function: list of check-function
    :param passwd:  password
    :return: result of check-functions
    '''
    for func in lst_of_function:
        if not func(passwd):
            return False
    return True

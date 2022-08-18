def is_incl_letter(passwd: str) -> bool:
    # At least 1 letter between [a-z] and 1 letter between [A-Z].
    flag_low = False
    flag_upp = False
    for i in passwd:
        if i.isalpha() and i.islower():
            flag_low = True
        if i.isalpha() and not i.islower():
            flag_upp = True
        if flag_low and flag_upp:
            return True
    else:
        print(f"Password need include at least 1 letter between [a-z] and 1 letter between [A-Z]")
        return False


def is_incl_digit(passwd: str) -> bool:
    # At least 1 number between [0-9].
    if any([str(num) in passwd for num in range(10)]):
        return True
    else:
        print(f"Password need include at least 1 number between [0-9]")
        return False


def is_incl_uniq(passwd: str) -> bool:
    # At least 1 character from [$ # @]
    for i in ['$', '#', '@']:
        if i in passwd:
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


LIST_OF_FUNCTION = (is_incl_letter, is_incl_digit, is_incl_uniq, check_lenght)
# List of check-functions


def correct_passwd(passwd: str, lst_of_function: list) -> bool:
    '''
    :param lst_of_function: list of check-function
    :param passwd:  password
    :return: result of check-functions
    '''
    return all([func(passwd) for func in lst_of_function])

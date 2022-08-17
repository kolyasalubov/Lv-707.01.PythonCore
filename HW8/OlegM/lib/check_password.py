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
    for i in passwd:
        if i.isdigit():
            return True
    else:
        print(f"Password need include at least 1 number between [0-9]")
        return False


def is_incl_uniq(passwd: str) -> bool:
    # At least 1 character from [$ # @]
    for i in passwd:
        if i in ['$', '#', '@']:
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


def correct_passwd(passwd: str) -> bool:
    return all([is_incl_letter(passwd), is_incl_digit(passwd), is_incl_uniq(passwd), check_lenght(passwd)])
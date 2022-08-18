import lib.check_password as check_pw

while not check_pw.correct_passwd(password := input("Enter your new password:"), check_pw.LIST_OF_FUNCTION):
    pass
else:
    print("Your password is SAFE!")
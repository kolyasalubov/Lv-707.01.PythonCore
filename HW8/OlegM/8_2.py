import lib.check_password as check_pw

#We can use function correct_passwd_short() for break after first False
while not check_pw.correct_passwd(password := input("\nEnter your new password:"), check_pw.LIST_OF_FUNCTION):
    pass
else:
    print("Your password is SAFE!")
import re



def check_pass():
    """The program for checking password"""
    print("This is the program for checking password \n\
           Here are the requirements for your password:\n\
           At least 1 letter between [a-z] and 1 letter between [A-Z].\n\
           At least 1 number between [0-9].\n\
           At least 1 character from [$#@].\n\
           Minimum length 6 characters.\n\
           Maximum length 16 characters.\n\n\n")
    while True:
        password=input("Enter your password here:")
        if re.findall("[a-z]" and "[A-Z]" and "[0-9]" and "[#,@,$]", password) and 6 < len(password) < 16:
         print(f"Your password is correct!\n Here is your password:{password}")
         break
        else:
            print("Your password does not satisfy the current policy requirements ")
    return password
        

check_pass()

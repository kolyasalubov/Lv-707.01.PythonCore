user_input_login = input("Enter your login,please: ")

while True:
    if user_input_login == "First":
        print(f"Hello {user_input_login}, Great works you are logged in")
        break
    else:
        print(f"You entered {user_input_login}, it's wrong login", end=" " )
        print(":Try again")
        user_input_login = input("Enter your login,please: ")

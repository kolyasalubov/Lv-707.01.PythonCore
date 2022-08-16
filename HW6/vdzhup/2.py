while True:
    user_password = input("Please enter the password: ")
    if user_password == "First":
        print("Congratulations! You have entered the correct password.")
        break
    else:
        print("You entered the wrong password. Try it again.")

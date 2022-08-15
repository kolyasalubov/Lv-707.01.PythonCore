while (str_login := input("Please enter users login:")) != "First":
    print("Password wrong! Try again!")
else:
    print(f"Hello {str_login}-user. How are you?")

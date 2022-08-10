enter_login: str = input("Please enter users login:")
while enter_login != "First":
    print("Password wrong! Try again!")
    enter_login: str = input("Please enter users login:")
else:
    print(f"Hello {enter_login}-user. How are you?")

# Task 2

username = "default"

while username != "First":
    username = input("Enter valid username: ")
    if username == "First":
        print(f"Username is correct. Welcome {username}.")
        break
    else:
        print("Username is incorrect. Try again.")
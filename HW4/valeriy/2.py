print("Enter correct username and password combo to continue")
count = 0
while count < 10:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if password =="Python707" and username =="Uchenik":
        print("Greetings!", username)
        break
    else:
        print("Access denied. Try again.")
        count += 1
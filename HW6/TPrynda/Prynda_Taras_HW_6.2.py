log_counter = 0
while True:
    list= input("Enter your login please:\nLogin:")
    if list == "First":
        print(f"Welcome, {list}! ")
        break
    else:
        log_counter+=1
        print("ERROR! WRONG LOGIN!")
    if log_counter >3:
        print("Too much TRIES, try to login later!")
        break
    

        

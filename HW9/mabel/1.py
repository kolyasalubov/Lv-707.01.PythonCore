from ast import While
import random 

random_num = random.randint(1,100)
print(random_num)
user_num = int(input("Enter your number"))


while random_num != user_num:
    if random_num < user_num:
        print("wrong!!number less")
        user_num = int(input("Enter your number"))
    elif random_num > user_num:
        print("wrong!!number is greater")
        user_num = int(input("Enter your number"))
else:
    print("Good")



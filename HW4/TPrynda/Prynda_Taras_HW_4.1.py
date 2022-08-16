num = int(input("Enter the number of factorial you want to count:"))

if num == 1 or num == 0:
    fact=1 
    print(f"Factorial {num}={fact}") 
elif num <0:
    print("There is no factorial of the negative number")
elif num>0:  
    fact = 1
    for i in range(1,num+1):
        fact*=i
        print(f"Factorial {i}={fact}")



        




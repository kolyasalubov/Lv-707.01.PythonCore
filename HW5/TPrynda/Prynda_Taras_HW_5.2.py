

num = 0
num_1 = 1  
range=int(input("Enter the number of Fibonacci sequence you want to get:\n"))


for i in range (2,range+1):
    fibo=num+num_1
    print(f"Fibonacci {i} = {fibo}")
    num=num_1
    num_1=fibo
    i+=1

